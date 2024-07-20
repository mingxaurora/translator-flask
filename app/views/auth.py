import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for 
)

from app import db
from app.models.auth_model import User  #絕對路徑
# from .. import db  #功能同上，為使用相對路徑。建議專案中盡量使用絕對路徑

#藍圖
bp = Blueprint('auth', __name__, url_prefix="/auth")


def login_required(view):
    '''
    用於確認使用者是否已登入的裝飾器，之後會添加到需要此功能的功能(路由)中。
    若使用者已登入，則會繼續執行功能；若沒有則重新導向登入頁面。
    '''
    #裝飾器用於包裝每個 view func (路由)，添加檢查登入功能。
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            #若沒有登入，則重新導向登入頁面
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
        error = None  #用於審核輸入帳密

        #確認是否有輸入帳號及密碼
        if not username:
            error = "Username is required."
        elif not password:
            error = "Password is required."
        elif db.session.execute(
            #db.select(User).filter_by(username=username) 會輸出 SQL 指令，例如 `SELECT "user".id, ...`
            #若想了解更多可自行設新路由拆解顯示 
            db.select(db.select(User).filter_by(username=username).exists())
        ).scalar():
            error = f"User {username} is already registered."

        #若輸入帳密無誤，完成註冊及重新導向至登入介面
        if error is None:
            db.session.add(User(username=username, password=password))
            db.session.commit()
            return redirect(url_for("auth.login"))

        #跳出警告訊息。另外，需在 HTML 檔中設定顯示的位置。
        flash(error)  

    return render_template("auth/register.html")  #flask 預設會從應用下的 templates 中找樣板，因此可從其路徑開始指定


@bp.route("/login", methods=("GET", "POST"))
def login():
    """登入已註冊的使用者，並將其添加至 session 中。"""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        error = None
        #用 username 從資料庫中尋找對應的資料
        select = db.select(User).filter_by(username=username)
        user = db.session.execute(select).scalar()

        if user is None:  #確認資料庫是否有此使用者
            error = "Incorrect username."
        elif not user.check_password(password):  #確認密碼是否正確
            error = "Incorrect password."

        if error is None:  
            #將使用者 ID 存儲在新的 session中，並返回到首頁。
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