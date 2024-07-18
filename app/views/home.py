from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from app import db
from app.models.history_model import History
from app.views.auth import login_required

bp = Blueprint('home', __name__)

#首頁
@bp.route('/')
def index():
    return render_template('base.html')  #


@bp.route('/test', methods=['GET', 'POST'])
def test_page():
    if request.method == 'POST':
        input_text = request.form['input_text']
        
        return render_template('test.html', output_text=input_text)
    
    return render_template('test.html')

@bp.route('/translate', methods=['POST'])
def translate():
    input_text = request.form['input_text']
    output = input_text


#測試
# @login_required
# @bp.route('/test', methods=("GET", "POST"))
# def index():
#     str1 = 'test'
#     print(str1)
#     return(str1)

