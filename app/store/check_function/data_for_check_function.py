from flask import request, session, redirect, url_for
from .tech_name import tech_name
from .tech_material import tech_material
from .tech_equipment import tech_equipment
from .tech_reel import tech_reel
def data_for_check_function():
    #filtramos los tecnicos en base del i
    tech_id = int(request.form['id_technical'])
    technical = session.get('technical')
    technical = tech_name(tech_id, technical)
    session['technical_name'] = technical
    technical = tech_material(tech_id)
    session['technical_materials'] = technical
    technical= tech_equipment(tech_id)
    session['technical_equipments'] = technical
    technical = tech_reel(tech_id)
    session['technical_reels'] = technical
    #revisamos los que funcion realizara para el tecnico
    return int(request.form['type_function'])