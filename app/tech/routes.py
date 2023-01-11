from . import tech
from flask import session, abort
from app.auth.routes import login_required
from app.auth.user_data import data_user

def requeriment():
    user = session.get('user')
    if user['position'] != 3:
        session.clear()
        abort(404)
        
@tech.route('/')
@login_required
def index():
    requeriment()
    data_user()
    return 'hola'