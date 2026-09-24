"""Database session management."""
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from backend.app.database.connection import engine

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_session() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session
