from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

from dotenv import load_dotenv
import os


class Base(DeclarativeBase):
    pass    
db = SQLAlchemy(model_class=Base)  #DB


def create_app(test_config=None):
    """建立並配置一個 Flask 應用程式的實體"""
    app = Flask(__name__)
    
    load_dotenv()  #從 .env 檔中載入環境變數道系統中。或者也可透過 set 指令直接設定變數值。
    db_url = os.environ.get("SQLALCHEMY_DATABASE_URI")  #從系統(shell)中找環境變數，可透過 set 指令設定變數值。
    #若沒有找到 db_url，則預設使用 sqlite
    if db_url is None: 
        db_url = "sqlite:///flaskr.sqlite"

    #應用載入配置
    app.config.from_mapping(
        # SECRET_KEY=os.environ.get("SECRET_KEY", "dev"),
        SQLALCHEMY_DATABASE_URI=db_url,
    )  
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)

    db.init_app(app)

    #套用藍圖到應用中
    from .views import home_bp

    app.register_blueprint(home_bp)
    app.add_url_rule("/", endpoint="index")

    return app

#初始化資料庫
def init_db():
    db.drop_all()
    db.create_all()

#定義 CLI 指令－初始化資料料庫
@click.command("init-db")
@with_appcontext
def init_db_command():
    """Clear existing data and create new tables."""
    init_db()
    click.echo("Initialized the database.")