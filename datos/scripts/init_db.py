#!/usr/bin/env python3
"""Inicializa (o reinicializa) la base de datos del mercado del cobre."""

import sys
from pathlib import Path

# Permitir ejecución directa: python datos/scripts/init_db.py
sys.path.insert(0, str(Path(__file__).resolve().parent))

from db import init_db, DB_PATH


def main():
    if DB_PATH.exists():
        print(f"Base existente encontrada: {DB_PATH}")
        resp = input("¿Reinicializar? Esto borra todos los datos. (s/N): ")
        if resp.lower() != "s":
            print("Cancelado.")
            return
        DB_PATH.unlink()
        print("Base anterior eliminada.")

    init_db()


if __name__ == "__main__":
    main()
