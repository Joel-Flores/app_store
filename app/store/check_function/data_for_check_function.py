from flask import request, session, redirect, url_for
from .tech_name import tech_name

def data_for_check_function():
    #filtramos los tecnicos en base del i
    tech_id = int(request.form['id_technical'])
    technical = session.get('technical')
    technical = tech_name(tech_id, technical)
    session['technical_name'] = technical
    #revisamos los que funcion realizara para el tecnico
    return int(request.form['type_function'])