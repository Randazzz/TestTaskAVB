from pydantic import BaseModel, HttpUrl


class URLRequest(BaseModel):
    url: HttpUrl


class ShortURLBase(BaseModel):
    short_url: HttpUrl


class ShortUrlResponse(ShortURLBase):
    pass
