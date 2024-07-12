from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)


bp = Blueprint('home', __name__)

#首頁
@bp.route('/')
def index():
    return render_template('base.html')  #


#測試
# @bp.route('/')
# def index():
#     str1 = 'test'
#     print(str1)
#     return(str1)

# @bp.route('/test_page')
# def test_page():
#     str1 = 'test_page'
#     print(str1)
#     return(str1)

