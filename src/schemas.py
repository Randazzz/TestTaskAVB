from pydantic import HttpUrl, BaseModel


class ShortUrlResponse(BaseModel):
    short_url: HttpUrl
