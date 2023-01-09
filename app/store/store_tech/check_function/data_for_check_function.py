"""
imoprtamos las herramientas necesarias
"""
from flask import request, session
from app.db import get_db
"""
importamos los modulos
"""
from .tech_name import tech_name
from .tech_material import tech_material
from .tech_equipment import tech_equipment
from .tech_reel import tech_reel

def data_for_check_function():
    db, c = get_db()
    #filtramos los tecnicos en base del i
    tech_id = int(request.form['id_technical'])
    
    #obtenemos los datos del tecnico
    session['technical_name'] = tech_name(tech_id, session.get('technical_active'))
    
    #obtenemos los materiales actuales que tiene el tecnico
    session['technical_materials'] = tech_material(c, tech_id)
    
    #obtenemos los equipos actuales que tiene el tecnico
    session['technical_equipments'] = tech_equipment(c, tech_id)
    
    #obtenemos las carretas actuales que tiene el tecnico
    session['technical_reels'] = tech_reel(c, tech_id)
    
    #revisamos los que funcion realizara para el tecnico
    return int(request.form['type_function'])