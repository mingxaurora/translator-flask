from flask import Flask
from flask.cli import with_appcontext  
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

import os
import click  
from dotenv import load_dotenv


class Base(DeclarativeBase):
    pass    
db = SQLAlchemy(model_class=Base)  


def create_app(test_config=None):
    """建立並配置一個 Flask 應用程式的實體"""
    app = Flask(__name__)
    
    load_dotenv()  
    db_url = os.environ.get("SQLALCHEMY_DATABASE_URI")  
    if db_url is None: 
        db_url = "sqlite:///flaskr.sqlite"


    app.config.from_mapping(
        SECRET_KEY=os.environ.get("SECRET_KEY", "dev"),  
        SQLALCHEMY_DATABASE_URI=db_url,
    )  
    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.update(test_config)


    db.init_app(app)  
    app.cli.add_command(init_db_command)  

    from .views import home_bp
    from .views import auth_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(auth_bp)
    app.add_url_rule("/", endpoint="index")

    return app


def init_db():
    db.drop_all()
    db.create_all()

@click.command("init-db")  
@with_appcontext  
def init_db_command():
    """Clear existing data and create new tables."""
    init_db()
    click.echo("Initialized the database.")