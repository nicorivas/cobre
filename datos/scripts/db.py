"""
db.py — Módulo central de acceso a la base de datos del mercado del cobre.

Provee:
  - connect()    → conexión DuckDB
  - init_db()    → crea schema desde schema.sql y carga seeds
  - ingest_raw() → escribe datos crudos a raw (append-only)
  - upsert_prices() / upsert_inventories() / upsert_cot() / upsert_macro()
                 → escribe a tablas clean con deduplicación
  - query()      → ejecuta SQL y retorna DataFrame
"""

from pathlib import Path
import duckdb
import pandas as pd
from dotenv import load_dotenv

# Paths relativos al repo
REPO_ROOT = Path(__file__).resolve().parent.parent.parent
DATOS_DIR = REPO_ROOT / "datos"

# Cargar .env (busca en datos/.env y en raíz del repo)
load_dotenv(DATOS_DIR / ".env")
load_dotenv(REPO_ROOT / ".env")
DB_PATH = DATOS_DIR / "cobre.duckdb"
SCHEMA_PATH = DATOS_DIR / "schema.sql"
SEEDS_DIR = DATOS_DIR / "seeds"


def connect(db_path: Path = DB_PATH, read_only: bool = False) -> duckdb.DuckDBPyConnection:
    return duckdb.connect(str(db_path), read_only=read_only)


def init_db(db_path: Path = DB_PATH):
    """Crea la base de datos desde schema.sql y carga seeds."""
    con = connect(db_path)

    # Ejecutar schema
    schema_sql = SCHEMA_PATH.read_text()
    # DuckDB no soporta múltiples statements en un solo execute,
    # pero sí con execute que parsea el script completo
    con.execute(schema_sql)

    # Cargar seed del catálogo de series
    catalog_csv = SEEDS_DIR / "series_catalog.csv"
    if catalog_csv.exists():
        df = pd.read_csv(catalog_csv)
        # Upsert: borrar y reinsertar para que el seed sea la fuente de verdad
        con.execute("DELETE FROM meta.series_catalog")
        con.execute(
            "INSERT INTO meta.series_catalog SELECT * FROM df"
        )

    con.close()
    print(f"Base de datos inicializada en {db_path}")
    print(f"  Schema: {SCHEMA_PATH}")
    print(f"  Series en catálogo: {len(df) if catalog_csv.exists() else 0}")


def ingest_raw(
    con: duckdb.DuckDBPyConnection,
    source: str,
    df: pd.DataFrame,
    notes: str | None = None,
) -> int:
    """
    Escribe datos crudos a raw.ingestions + raw.series_data.

    df debe tener columnas: series_id, trade_date, value
    Columnas opcionales: high, low, volume, unit

    Retorna el ingestion_id.
    """
    con.execute(
        """
        INSERT INTO raw.ingestions (source, fetched_at, status, row_count, notes)
        VALUES (?, now(), 'ok', ?, ?)
        """,
        [source, len(df), notes],
    )
    ingestion_id = con.execute(
        "SELECT max(ingestion_id) FROM raw.ingestions"
    ).fetchone()[0]

    # Asegurar columnas opcionales
    for col in ["high", "low", "volume", "unit"]:
        if col not in df.columns:
            df[col] = None

    raw_df = df[["series_id", "trade_date", "value", "high", "low", "volume", "unit"]].copy()
    raw_df["ingestion_id"] = ingestion_id

    con.execute(
        """
        INSERT INTO raw.series_data
            (ingestion_id, series_id, trade_date, value, high, low, volume, unit)
        SELECT ingestion_id, series_id, trade_date, value, high, low, volume, unit
        FROM raw_df
        """
    )
    return ingestion_id


def upsert_prices(con: duckdb.DuckDBPyConnection, df: pd.DataFrame):
    """
    Upsert a clean.prices.

    df debe tener: trade_date, series_id, close
    Opcionales: high, low, volume, unit
    """
    for col, default in [("high", None), ("low", None), ("volume", None), ("unit", "usd_per_ton")]:
        if col not in df.columns:
            df[col] = default

    con.execute(
        """
        INSERT OR REPLACE INTO clean.prices
            (trade_date, series_id, close, high, low, volume, unit, updated_at)
        SELECT trade_date, series_id, close, high, low, volume, unit, now()
        FROM df
        """
    )


def upsert_inventories(con: duckdb.DuckDBPyConnection, df: pd.DataFrame):
    """
    Upsert a clean.inventories.

    df debe tener: trade_date, exchange, category, volume_mt
    """
    con.execute(
        """
        INSERT OR REPLACE INTO clean.inventories
            (trade_date, exchange, category, volume_mt, updated_at)
        SELECT trade_date, exchange, category, volume_mt, now()
        FROM df
        """
    )


def upsert_cot(con: duckdb.DuckDBPyConnection, df: pd.DataFrame):
    """
    Upsert a clean.cot.

    df debe tener: report_date, managed_money_long, managed_money_short,
                   managed_money_net, producer_long, producer_short, producer_net,
                   total_oi
    Opcionales: swap_dealer_long, swap_dealer_short, swap_dealer_net
    """
    for col in ["swap_dealer_long", "swap_dealer_short", "swap_dealer_net"]:
        if col not in df.columns:
            df[col] = None

    con.execute(
        """
        INSERT OR REPLACE INTO clean.cot
            (report_date, managed_money_long, managed_money_short, managed_money_net,
             producer_long, producer_short, producer_net,
             swap_dealer_long, swap_dealer_short, swap_dealer_net,
             total_oi, updated_at)
        SELECT report_date, managed_money_long, managed_money_short, managed_money_net,
               producer_long, producer_short, producer_net,
               swap_dealer_long, swap_dealer_short, swap_dealer_net,
               total_oi, now()
        FROM df
        """
    )


def upsert_macro(con: duckdb.DuckDBPyConnection, df: pd.DataFrame):
    """
    Upsert a clean.macro.

    df debe tener: obs_date, series_id, value
    """
    con.execute(
        """
        INSERT OR REPLACE INTO clean.macro (obs_date, series_id, value, updated_at)
        SELECT obs_date, series_id, value, now()
        FROM df
        """
    )


def upsert_spreads(con: duckdb.DuckDBPyConnection, df: pd.DataFrame):
    """
    Upsert a clean.spreads.

    df debe tener: trade_date, spread_id, value
    Opcionales: unit
    """
    if "unit" not in df.columns:
        df["unit"] = None

    con.execute(
        """
        INSERT OR REPLACE INTO clean.spreads (trade_date, spread_id, value, unit, updated_at)
        SELECT trade_date, spread_id, value, unit, now()
        FROM df
        """
    )


def query(sql: str, db_path: Path = DB_PATH, params: list | None = None) -> pd.DataFrame:
    """Ejecuta SQL de lectura y retorna DataFrame."""
    con = connect(db_path, read_only=True)
    result = con.execute(sql, params or []).fetchdf()
    con.close()
    return result
