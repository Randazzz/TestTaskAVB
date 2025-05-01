import httpx
from fastapi import APIRouter, status, Depends

from src.api.v1.dependecies import get_external_api_service
from src.api.v1.external_api.schemas import CatFactResponse
from src.api.v1.external_api.service import ExternalAPIService

router = APIRouter()


@router.get(
    "/cat-fact",
    response_model=CatFactResponse,
    status_code=status.HTTP_200_OK,
    summary="Get a fact about cats",
)
async def get_cat_fact(external_api_service: ExternalAPIService = Depends(get_external_api_service),):
    return await external_api_service.get_cat_fact_or_raise()
