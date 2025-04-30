from fastapi import APIRouter, Depends, status
from fastapi.responses import RedirectResponse

from src.api.v1.url_shortener.schemas import ShortUrlResponse, URLRequest
from src.api.v1.url_shortener.service import URLShortenerService
from src.api.v1.dependecies import get_url_shortener_service

router = APIRouter()


@router.post(
    "/",
    response_model=ShortUrlResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create short url",
)
async def create_short_url(
    data: URLRequest,
    url_shortener_service: URLShortenerService = Depends(get_url_shortener_service),
):
    short_key = await url_shortener_service.create(data.url)
    return {"short_url": f"http://127.0.0.1:8080/{short_key}"}


@router.get(
    "/{short_id}",
    status_code=status.HTTP_307_TEMPORARY_REDIRECT,
    summary="Redirect to original",
)
async def redirect_to_original(
    short_id: str,
    url_shortener_service: URLShortenerService = Depends(get_url_shortener_service),
):
    original_url = await url_shortener_service.get_by_short_id_or_raise(short_id)
    return RedirectResponse(original_url, status_code=307)
