"""
imoprtamos las herramientas necesarias
"""
from app.db import get_db
from flask import session, render_template
"""
importamos los modulos
"""
from .data_technicals import data_technical
def logic_index():
    db , c = get_db()
    #guarda el id , nombre, apellido de los tecnicos
    session['technical_active'] = data_technical(c)
    #sacamos la version json del la consulta
    json = dict()
    json['user'] = session.get('user')
    json['materials'] = session.get('materials')
    json['equipment_count'] = session.get('equipment_count')
    json['technical_active'] = session.get('technical_active')
    #return json
    return render_template('/store/index.html')