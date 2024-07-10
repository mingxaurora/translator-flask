from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String, URL
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional

class Base(DeclarativeBase):
    pass    
db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
url_object = URL.create(  
    "mysql+pymysql",
    username="ming",
    password="1234",  # 純文字（未轉譯符號）
    host="localhost", #localhost or 3306
    database="geeklogin",
)  #登入配置也許可改成讀取金鑰的方式
app.config['SQLALCHEMY_DATABASE_URI'] = url_object
db.init_app(app)

class User(db.Model):  #也可以直接繼承 Base
    __tablename__ = "user_account"  #不一定要有，如果沒有指定名稱則會直接使用類別名稱
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(30), unique=True)
    # email: Mapped[Optional[str]]  #使用 Optional[] 讓欄位可以是 null。 目前無法使用，可能是bug
    
with app.app_context():
    db.create_all()