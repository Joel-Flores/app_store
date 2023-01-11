#importar la configurcion del blueprint
from . import store
from flask import session
from app.auth.routes import login_required
#funcion para la ruta de index
from .index import logic_index

def requeriment():
    user = session.get('user')
    if user['position'] != 2:
        session.clear()
"""
pagina pricipal del almacen"""
@store.route('/')
@login_required
def index():
    requeriment()
    return logic_index()
