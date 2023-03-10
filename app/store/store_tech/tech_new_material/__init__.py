from flask import request, session, g, redirect, url_for
from app.auth.user_data import data_user

from .assign_teams import assign_teams
from .assign_materials import assign_materials
from .assign_reels import assign_reels

def logic_tech_new_material():
    user_id = g.user['id']
    name_tech = session.get('technical_name')
    material_tech = session.get('technical_materials')
    #actualizamos y registramos los materiales de tecnico y del almacen
    message_1 = assign_materials(session.get('materials'), user_id, material_tech, name_tech)
    
    #agrega los equipos al tecnico o manda un mensaje de el equipo no se encuantra en el almacen
    message_2 = assign_teams(request.form['series'].split("\r\n"), name_tech, user_id)
    
    #agrega las carretas al tecnico y los desvincula del almacen
    message_3 = assign_reels(request.form['reels'].split("\r\n"), name_tech, user_id)
    
    #actulaziar los datos del almacen
    data_user()
    messages = message_1 + message_2 + message_3
    response = redirect(url_for('store.index'))
    return response, messages