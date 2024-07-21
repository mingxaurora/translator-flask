import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for 
)

from app import db
from app.models.auth_model import User  

bp = Blueprint('auth', __name__, url_prefix="/auth")


def login_required(view):
    '''
    用於確認使用者是否已登入的裝飾器，之後會添加到需要此功能的功能(路由)中。
    若使用者已登入，則會繼續執行功能；若沒有則重新導向登入頁面。
    '''
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view


@bp.before_app_request
def load_logged_in_user():
    '''
    此裝飾器用於註冊一個函式在應用程序請求之前執行，
    在這裡我們將在請求前先從 session 中載入使用者的資訊
    '''
    user_id = session.get("user_id")  

    if user_id is not None:
        g.user = db.session.get(User, user_id)
    else:
        g.user = None


@bp.route("/register", methods=("GET", "POST"))
def register():
    """註冊新使用者。
    驗證使用者使用者名稱未被使用。為了安全，雜湊化密碼。
    """
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        error = None  

        if not username:
            error = "Username is required."
        elif not password:
            error = "Password is required."
        elif db.session.execute(
            db.select(db.select(User).filter_by(username=username).exists())
        ).scalar():
            error = f"User {username} is already registered."

        if error is None:
            db.session.add(User(username=username, password=password))
            db.session.commit()
            return redirect(url_for("auth.login"))

        flash(error)  

    return render_template("auth/register.html")  


@bp.route("/login", methods=("GET", "POST"))
def login():
    """登入已註冊的使用者，並將其添加至 session 中。"""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        error = None
        select = db.select(User).filter_by(username=username)
        user = db.session.execute(select).scalar()

        if user is None:  
            error = "Incorrect username."
        elif not user.check_password(password):  
            error = "Incorrect password."

        if error is None:  
            session.clear()
            session["user_id"] = user.id
            return redirect(url_for("index"))

        flash(error)

    return render_template("auth/login.html")


@bp.route("/logout")
def logout():
    """清除當前 session(例如：使用者 ID)."""
    session.clear()
    return redirect(url_for("index"))