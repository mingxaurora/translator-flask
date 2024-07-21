from __future__ import annotations  
from typing import TYPE_CHECKING

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

from app import db

if TYPE_CHECKING:
    from .history_model import History


class User(db.Model):  
    # __tablename__ = "user_account"  
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(30), unique=True)
    password_hash: Mapped[str] = mapped_column(String(255))
    
    histories : Mapped[list[History]] = relationship('History', back_populates='owner')  

    @property
    def password(self):
        raise AttributeError('passowrd is not readabilty attribute')
    
    @password.setter
    def password(self, value: str) -> None:
        """Store the password as a hash for security."""
        self.password_hash = generate_password_hash(value)

    def check_password(self, value: str) -> bool:
        '''比對註冊密碼和輸入密碼'''
        return check_password_hash(self.password_hash, value)

