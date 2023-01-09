from flask import request, session, g, redirect, url_for
from app.auth.user_data import data_user

from .assign_materials import assign_materials
from .assign_teams import assign_teams
from .assign_reel import assign_reel

from .request_equipment import request_equipment
from .request_reel_withdraw import request_reel_withdraw
def logic_tech_withdraw_material():
    #datos para las funciones
    user_id = g.user['id']
    user_material = session.get('materials')
    tech_name = session.get('technical_name')
    tech_material = session.get('technical_materials')
    tech_equiment = session.get('technical_equipments')
    tech_reel = session.get('technical_reels')
    
    #retirar materiales al tecnico
    assign_materials(user_id, user_material, tech_name, tech_material)
    #retiramos equipos del tecnico
    assign_teams(user_id, tech_name, tech_equiment)
    #retiramos carretas del tecnico
    assign_reel(user_id, tech_name, tech_reel)
    #actulaziar los datos del almacen
    data_user()
    return redirect(url_for('store.index'))