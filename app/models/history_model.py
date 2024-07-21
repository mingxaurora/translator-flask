# from __future__ import annotations
from typing import TYPE_CHECKING

from datetime import datetime
from datetime import timezone
from sqlalchemy import Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app import db
from app.models.auth_model import User

# if TYPE_CHECKING:
#     from .auth_model import User


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


class History(db.Model):
    # __tablename__ = ""
    id: Mapped[int] = mapped_column(primary_key=True)
    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey('user.id'))
    original_text: Mapped[str] = mapped_column(String(255))
    translated_text: Mapped[str] = mapped_column(String(255))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=now_utc)

    owner: Mapped[User] = relationship(lazy="joined", back_populates='histories')


