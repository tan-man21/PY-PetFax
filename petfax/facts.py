from flask import (Blueprint, render_template)

bp = Blueprint('fact', __name__, url_prefix='/facts')

@bp.route('/')
def index():
    return f'These are all the facts'

@bp.route('/new')
def new():
    return render_template('facts/new.html')