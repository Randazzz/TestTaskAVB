from pydantic import BaseModel, HttpUrl


class ShortUrlResponse(BaseModel):
    short_url: HttpUrl
