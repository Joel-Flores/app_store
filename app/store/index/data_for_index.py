"""
imoprtamos las herramientas necesarias
"""
from app.db import get_db
from flask import g, session
"""
importamos los modulos
"""
from .data_technicals import data_technical
from .count_reel import count_reel
def data_for_index():
    db , c = get_db()
    #guarda el id , nombre, apellido de los tecnicos
    session['technical'] = data_technical(c)
    #guarda la catidad de carretas en almacen
    session['count_reel'] = count_reel(c, g.user['id'])