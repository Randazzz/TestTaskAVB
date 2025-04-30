import uvicorn
from fastapi import FastAPI

from src.api.v1 import router as v1_router
from src.config import settings

app = FastAPI(debug=settings.DEBUG)

app.include_router(v1_router)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)
