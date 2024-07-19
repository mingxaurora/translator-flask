from flask import (
    Blueprint, flash, g, redirect, render_template, request,session ,url_for
)

from app.until.translation import translate_func

from app import db
from app.models.history_model import History
from app.views.auth import login_required

bp = Blueprint('home', __name__)

#首頁
@bp.route('/')
def index():
    translated_text = request.args.get('translated_text')
    datas = {
        'translated_text': translated_text
    }
    return render_template('home/index.html', **datas)

# @bp.route('/test_page')
# def test_page():
#     translated_text = request.args.get('translated_text')
#     datas = {
#         'translated_text': translated_text
#     }
#     return render_template('test.html', **datas) 

@bp.route('/test', methods=['POST'])
def translate():
    original_text = request.form['original_text']
    error = None

    if not original_text:
        error = 'Please enter text first'
    if error != None:
        flash(error)
    else:   
        translated_text = translate_func(original_text)
        if g.user != None:
            db.session.add(History(
                original_text=original_text, 
                translated_text=translated_text, 
                owner=g.user  #不會直接出現在資料表中
            ))
            db.session.commit()

        return redirect(url_for('home.index', translated_text=translated_text))

    return render_template('home/index.html')




#測試
# @login_required
# @bp.route('/test', methods=("GET", "POST"))
# def index():
#     str1 = 'test'
#     print(str1)
#     return(str1)

