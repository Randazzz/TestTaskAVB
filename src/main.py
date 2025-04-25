from contextlib import asynccontextmanager
from typing import AsyncIterator

import uvicorn
from fastapi import FastAPI
from redis import RedisError
from redis import asyncio as redis

from src.api import router


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    redis_client = redis.Redis(host="redis", decode_responses=True)
    try:
        await redis_client.ping()
        app.state.redis = redis_client
        print("Successfully connected to Redis!")
    except RedisError as e:
        print(f"Failed to connect to Redis: {type(e).__name__}: {str(e)}")
        raise RuntimeError(f"Redis connection error: {e}")
    yield
    await redis_client.close()


app = FastAPI(lifespan=lifespan)

app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)
