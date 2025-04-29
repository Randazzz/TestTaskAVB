import httpx
from fastapi import APIRouter, status

router = APIRouter()


@router.get(
    "/cat-fact/",
    status_code=status.HTTP_200_OK,
    summary="Get a fact about cats",
)
async def get_cat_fact():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://catfact.ninja/fact")
        return response.json()
