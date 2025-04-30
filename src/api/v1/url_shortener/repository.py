from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.v1.url_shortener.models import ShortenedURL


class URLShortenerRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, shortened_url: ShortenedURL) -> ShortenedURL:
        self.db.add(shortened_url)
        await self.db.commit()
        await self.db.refresh(shortened_url)
        return shortened_url

    async def get_by_short_id_or_none(self, short_id):
        stmt = select(ShortenedURL).filter(ShortenedURL.short_key == short_id)  # type: ignore
        result = await self.db.execute(stmt)
        shortened_url = result.scalars().first()
        if not shortened_url:
            return None
        return shortened_url

    async def get_by_original_url_or_none(self, original_url):
        stmt = select(ShortenedURL).filter(ShortenedURL.original_url == original_url)  # type: ignore
        result = await self.db.execute(stmt)
        shortened_url = result.scalars().first()
        if not shortened_url:
            return None
        return shortened_url
