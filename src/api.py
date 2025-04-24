import uuid

import httpx
from fastapi import APIRouter, HTTPException, status, Response
from fastapi.responses import RedirectResponse
from pydantic import HttpUrl

from src.schemas import ShortUrlResponse

router = APIRouter(tags=["api"])

db = {}


@router.post(
    "/",
    response_model=ShortUrlResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create short url",
)
async def create_short_url(url: HttpUrl):
    for short_id, db_url in db.items():
        if url == db_url:
            return {"short_url": f"http://127.0.0.1:8080/{short_id}"}
    short_id = str(uuid.uuid4())[:8]
    db[short_id] = url
    return {"short_url": f"http://127.0.0.1:8080/{short_id}"}


@router.get(
    "/{short_id}",
    status_code=status.HTTP_307_TEMPORARY_REDIRECT,
    summary="Redirect to original",
)
async def redirect_to_original(short_id: str):
    try:
        original_url = db[short_id]
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return RedirectResponse(original_url, status_code=307)


@router.get(
    "/cat-fact/",
    status_code=status.HTTP_200_OK,
    summary="Get a fact about cats"
)
async def get_cat_fact():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://catfact.ninja/fact")
        return response.json()
