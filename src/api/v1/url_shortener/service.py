from pydantic import HttpUrl
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.v1.url_shortener.models import ShortenedURL
from src.api.v1.url_shortener.repository import URLShortenerRepository


class URLShortenerService:
    def __init__(self, db: AsyncSession):
        self.url_shortener_repo = URLShortenerRepository(db)

    async def create(self, url: HttpUrl) -> str:
        shortened_url = ShortenedURL(
            original_url=str(url),
        )
        shortened_url_db = await self.url_shortener_repo.create(shortened_url)
        return shortened_url_db.short_key

    async def get_by_short_id_or_raise(self, short_id):
        shortened_url = await self.url_shortener_repo.get_by_short_id_or_none(short_id)
        return shortened_url.original_url
