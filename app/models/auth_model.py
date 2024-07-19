from __future__ import annotations  #匯入撰寫型別註解的功能。Python3.7之前才需要。
from typing import TYPE_CHECKING

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

from app import db

# 不是真的匯入，而是讓型別檢查工具知道此型別 (Post) 的存在
if TYPE_CHECKING:
    from .history_model import History


class User(db.Model):  #也可以直接繼承 Base
    # __tablename__ = "user_account"  #不一定要有，如果沒有指定名稱則會直接使用類別名稱
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(30), unique=True)
    password_hash: Mapped[str] = mapped_column(String(255))
    #relationship()之參數，'History' 為關聯模型名稱，owner 關聯的表格列名。
    #histories 不會直接變成資料表的欄位，推測僅僅是用於確認關聯
    histories : Mapped[list[History]] = relationship('History', back_populates='owner')  #Mapped[] ...。list[History] 用於指定提取的 History 的儲存方式。

    @property
    def password(self):
        raise AttributeError('passowrd is not readabilty attribute')
    
    @password.setter
    def password(self, value: str) -> None:
        """Store the password as a hash for security."""
        self.password_hash = generate_password_hash(value)

    def check_password(self, value: str) -> bool:
        return check_password_hash(self.password_hash, value)

