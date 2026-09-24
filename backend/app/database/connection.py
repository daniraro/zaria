"""Database connection setup."""
from sqlalchemy.ext.asyncio import create_async_engine
from backend.app.config import settings

engine = create_async_engine(settings.DATABASE_URL, echo=settings.DEBUG)
