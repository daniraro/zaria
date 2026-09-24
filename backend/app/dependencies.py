"""Common dependencies for dependency injection."""
from typing import Annotated
from fastapi import Depends


async def get_current_user(token: Annotated[str, Depends()]):
    """Get current authenticated user from token."""
    return {"user_id": 1, "username": "demo"}


async def get_db_session():
    """Get database session."""
    pass
