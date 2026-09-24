#!/usr/bin/env python3
"""Script para backup do banco de dados."""

import subprocess
from datetime import datetime
from pathlib import Path

BACKUP_DIR = Path(__file__).parent.parent / "backups"
BACKUP_DIR.mkdir(exist_ok=True)


def run_backup(db_name: str, db_user: str):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = BACKUP_DIR / f"{db_name}_{timestamp}.sql"

    cmd = [
        "pg_dump",
        "-U", db_user,
        "-d", db_name,
        "-f", str(backup_file)
    ]

    subprocess.run(cmd, check=True)
    print(f"Backup realizado: {backup_file}")


if __name__ == "__main__":
    run_backup("zaria", "postgres")
