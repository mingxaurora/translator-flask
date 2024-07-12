
from sqlalchemy.orm import Mapped, mapped_column, relationship
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

from flaskr import db



class User(db.Model):  #也可以直接繼承 Base
    # __tablename__ = "user_account"  #不一定要有，如果沒有指定名稱則會直接使用類別名稱
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(30), unique=True)
    password_hash: Mapped[str]

    @property
    def password(self):
        raise AttributeError('passowrd is not readabilty attribute')
    
    @password.setter
    def password(self, value: str) -> None:
        """Store the password as a hash for security."""
        self.password_hash = generate_password_hash(value)

    def check_password(self, value: str) -> bool:
        return check_password_hash(self.password_hash, value)

