import uuid

from fastapi import APIRouter, HTTPException, Request, status
from fastapi.responses import RedirectResponse
from pydantic import HttpUrl

from src.api.v1.url_shortener.schemas import ShortUrlResponse

router = APIRouter()


@router.post(
    "/",
    response_model=ShortUrlResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create short url",
)
async def create_short_url(url: HttpUrl, request: Request):
    url = str(url)
    redis_client = request.app.state.redis
    short_id = await redis_client.get(url)

    if short_id is None:
        short_id = str(uuid.uuid4())[:8]
        await redis_client.set(url, short_id)
        await redis_client.set(short_id, url)
    return {"short_url": f"http://127.0.0.1:8080/{short_id}"}


@router.get(
    "/{short_id}",
    status_code=status.HTTP_307_TEMPORARY_REDIRECT,
    summary="Redirect to original",
)
async def redirect_to_original(short_id: str, request: Request):
    redis_client = request.app.state.redis
    original_url = await redis_client.get(short_id)

    if original_url is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return RedirectResponse(original_url, status_code=307)
