from flask import (
    Blueprint, flash, g, redirect, render_template, request,session ,url_for
)

from app.utils.translation import translate_func

from app import db
from app.models.history_model import History
# from app.views.auth import login_required

bp = Blueprint('home', __name__)


@bp.route('/')
def index():

    translated_text = request.args.get('translated_text')
    if session.get("user_id"):
        select = db.select(History) \
            .where(History.owner_id == session["user_id"]) \
            .order_by(History.created_at.desc())
        historys = db.session.execute(select).scalars()
    else:
        historys = None
    
    datas = {
        'translated_text': translated_text,
        'historys': historys
    }

    return render_template('home/index.html', **datas)


@bp.route('/translate', methods=['POST'])
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
                owner=g.user  
            ))
            db.session.commit()

        return redirect(url_for('home.index', translated_text=translated_text))

    return render_template('home/index.html')
