from flask import request, session, g, redirect, url_for
from app.auth.user_data import data_user

from . import assign_materials
from . import assign_teams
from . import assign_reel

def logic_tech_withdraw_material():
    #datos para las funciones
    user_id = g.user['id']
    user_material = session.get('materials')
    tech_name = session.get('technical_name')
    tech_material = session.get('technical_materials')
    tech_equiment = session.get('technical_equipments')
    tech_reel = session.get('technical_reels')
    
    #retirar materiales al tecnico
    message_1 = assign_materials.assign_materials(user_id, user_material, tech_name, tech_material)
    #retiramos equipos del tecnico
    message_2 = assign_teams.assign_teams(user_id, tech_name, tech_equiment)
    #retiramos carretas del tecnico
    message_3 = assign_reel.assign_reel(user_id, tech_name, tech_reel)
    #actulaziar los datos del almacen
    data_user()
    message = message_1 + message_2 + message_3
    response = redirect(url_for('store.index'))
    return response, message