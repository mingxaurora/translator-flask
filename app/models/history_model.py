# from __future__ import annotations
from typing import TYPE_CHECKING

from datetime import datetime
from datetime import timezone
from sqlalchemy import Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app import db
from app.models.auth_model import User

#好像不用這段
# # 不是真的匯入，而是讓型別檢查工具知道此型別 (Post) 的存在
# if TYPE_CHECKING:
#     from .auth_model import User


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


class History(db.Model):
    # __tablename__ = ""
    id: Mapped[int] = mapped_column(primary_key=True)
    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey('user.id'))
    original_text: Mapped[str] = mapped_column(String(255))
    translation_text: Mapped[str] = mapped_column(String(255))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=now_utc)

    #author_id 支持的使用者物件
    #lazy="joined"，表示執行查詢時 User 會連同 History 一同回傳。
    owner: Mapped[User] = relationship(lazy="joined", back_populates='histories')
    # owner: Mapped[User] = relationship('User', back_populates='histories')  #需確認跟以上的差異


