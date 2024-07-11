# flaskapp_test

練習以 MVC 架構完成一個專案。

## Config

**DB URL 設定**

可直接透過以下指令設定 shell 的環境變數 (舉例)：
```
$env:SQLALCHEMY_DATABASE_URI = "mysql+pymysql://ming:1234@localhost/geeklogin"
```
或者，寫在 .env 檔中。

# Run

Windows cmd:
```
set FLASK_APP=flaskr
set FLASK_ENV=development
flask init-db
flask run
```
Open http://127.0.0.1:5000 in a browser.

_________
## 參考架構

來源：https://www.maxlist.xyz/2020/05/24/flask-session-base-login/
