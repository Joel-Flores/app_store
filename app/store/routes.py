from . import store
from flask import session, abort
from app.auth.routes import login_required

from .route_index import get_index

def requeriment():
    user = session.get('user')
    if user['position'] != 2:
        session.clear()
        abort(404)        

"""
pagina pricipal del almacen"""
@store.route('/')
@login_required
def index():
    requeriment()
    return get_index()
