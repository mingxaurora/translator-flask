# Translator-Flask

## Description

### 敘述
此專案主要用途圍繞在翻譯及相關延伸功能上。

### 開發成果說明
- 使用 Flask 開發路由，包括：串接各個對應頁面、專案核心功能。
- 各頁面 HTML、CSS 完成撰寫。以 Jinja2  模板引擎撰寫 HTML。
- 以 MVC 架構開發專案，在專案中明確分類不同用途的檔案。
- 以 ORM 技術實現資料庫的存取及操作。
- 串接資料庫 (MySQL)：
	- 註冊資料儲存至資料庫。
	- 登入時比對資料庫中的使用者帳密。
	- 使用者翻譯紀錄儲存至資料庫。
- 利用 Session 記憶登入的使用者，並用於追蹤資料庫中對應的資料。
	- 登入不同的使用者，可頁面中顯示不同的資料。
- 利用 transformers 庫實現翻譯功能。

### 使用之工具(套件、框架)：
- Flask
- SQLAlchemy
- Flask-SQLAlchemy
- Jinja2
- MySQL
- Transformers

### 未來
由於 LLM 的性能對於翻譯的表現越來越優異，因此未來會結合更多 LLM 實現更多其他功能，包含截圖翻譯、多語言精確翻譯、譯文語音生成等等。

## Demo

https://github.com/user-attachments/assets/e2276a2c-a5be-4735-bdda-e04af8c33bc8

## Config

**DB URL 設定**

可直接透過以下指令設定 shell 的環境變數 (舉例)：
```
$env:SQLALCHEMY_DATABASE_URI = "mysql+pymysql://ming:1234@localhost/geeklogin"
```
或者，寫在 .env 檔中。

## Run

Windows cmd:
```
set FLASK_APP=flaskr
set FLASK_ENV=development
flask init-db
flask run
```
Open http://127.0.0.1:5000 in a browser.


