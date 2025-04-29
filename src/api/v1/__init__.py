from fastapi import APIRouter

from .external_api.router import router as external_api_router
from .url_shortener.router import router as url_shortener_router

router = APIRouter(prefix="/api/v1")

router.include_router(url_shortener_router, prefix="/short-url", tags=["URL Shortener"])
router.include_router(external_api_router, prefix="/external", tags=["External APIs"])
