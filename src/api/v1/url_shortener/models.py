from sqlalchemy import BigInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from src.api.v1.url_shortener.utils import generate_short_key
from src.database import Base


class ShortenedURL(Base):
    __tablename__ = "shortened_urls"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    short_key: Mapped[str] = mapped_column(
        String(8),
        unique=True,
        index=True,
        default=lambda: generate_short_key(8)
    )
    original_url: Mapped[str] = mapped_column(String(2048), nullable=False, unique=True)
