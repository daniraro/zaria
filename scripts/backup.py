"""Backup script for database."""
import asyncio
import subprocess
from datetime import datetime
from backend.app.config import settings


async def create_backup():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = f"backup_zaria_{timestamp}.sql"
    cmd = f"pg_dump {settings.DATABASE_URL} > {backup_file}"
    
    try:
        subprocess.run(cmd, shell=True, check=True)
        print(f"✅ Backup created: {backup_file}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Backup failed: {e}")


if __name__ == "__main__":
    asyncio.run(create_backup())
