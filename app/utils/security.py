from fastapi import HTTPException, Security, status
from fastapi.security import APIKeyHeader

from app.config import settings

# Task 1: declare the header. This is what powers the Authorize button in /docs.
api_key_header = APIKeyHeader(name="X-API-Key")


async def verify_api_key(api_key: str | None = Security(api_key_header)) -> str:
    """Resolve an API key to an internal user id.

    A missing header already returns 401 before this code runs.
    An unknown key returns 403. The raw key never leaves this function.
    """
    user_id = settings.api_keys.get(api_key)
    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid API key.",
        )
    return user_id