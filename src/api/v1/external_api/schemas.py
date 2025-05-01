from pydantic import BaseModel


class CatFactResponse(BaseModel):
    fact: str
    length: int
