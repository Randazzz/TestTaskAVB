from typing import Callable, Type, TypeVar

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.v1.url_shortener.service import URLShortenerService
from src.database import get_db

T = TypeVar("T")


def get_service(service_class: Type[T]) -> Callable[[AsyncSession], T]:
    def _get_service(db: AsyncSession = Depends(get_db)) -> T:
        return service_class(db)

    return _get_service


get_url_shortener_service = get_service(URLShortenerService)
