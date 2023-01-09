from flask import request, session, g, redirect, url_for
from app.auth.user_data import data_user

from .assign_materials import assign_materials
from .assign_teams import assign_teams

from .request_equipment import request_equipment
from .request_reel_withdraw import request_reel_withdraw
def logic_tech_withdraw_material():
    ''' #retirar materiales al tecnico
    assign_materials(g.user['id'], session.get('materials'), session.get('technical_name'), session.get('technical_materials'))
    #retiramos equipos del tecnico
    assign_teams(g.user['id'], session.get('technical_name'), session.get('technical_equipments')) '''
    
    serial = request_equipment(session.get('technical_equipments'))
    reel = request_reel_withdraw(session.get('technical_reels'))
    json = dict()
    json['serials'] = serial
    json['reel'] = reel
    return json
    ''' #actulaziar los datos del almacen
    data_user()
    return redirect(url_for('store.index')) '''