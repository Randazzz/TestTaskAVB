import logging

import httpx
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

logger = logging.getLogger(__name__)


class ExternalAPIService:
    def __init__(self, db: AsyncSession):
        pass

    @staticmethod
    async def get_cat_fact_or_raise() -> dict:
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get("https://catfact.ninja/fact")
                response.raise_for_status()
                return response.json()
        except httpx.HTTPError as e:
            logger.error(f"Failed to fetch cat fact: {e}")
            raise HTTPException(status_code=503, detail=f"Failed to fetch cat fact")
