from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String, URL
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional

from dotenv import load_dotenv
import os


class Base(DeclarativeBase):
    pass    
db = SQLAlchemy(model_class=Base)

def create_app():
    """Create and configure an instance of the Flask application."""
     app = Flask(__name__)
    
    load_dotenv()  #從 .env 檔中載入環境變數道系統中。或者也可透過 set 指令直接設定變數值。
    db_url = os.environ.get("SQLALCHEMY_DATABASE_URI")  #從系統(shell)中找環境變數，可透過 set 指令設定變數值。
    #若沒有找到 db_url，則預設使用 sqlite
    if db_url is None: 
        db_url = "sqlite:///flaskr.sqlite"

    app.config.from_mapping(
        # SECRET_KEY=os.environ.get("SECRET_KEY", "dev"),
        SQLALCHEMY_DATABASE_URI=db_url,
    )  

    db.init_app(app)

    app.add_url_rule("/", endpoint="index")

    return app


# class User(db.Model):  #也可以直接繼承 Base
#     __tablename__ = "user_account"  #不一定要有，如果沒有指定名稱則會直接使用類別名稱
#     id: Mapped[int] = mapped_column(primary_key=True)
#     username: Mapped[str] = mapped_column(String(30), unique=True)
#     # email: Mapped[Optional[str]]  #使用 Optional[] 讓欄位可以是 null。 目前無法使用，可能是bug
    
# with app.app_context():
#     db.create_all()