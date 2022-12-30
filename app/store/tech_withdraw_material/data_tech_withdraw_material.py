from flask import session

from .assign_materials import assign_materials
from .assign_teams import assign_teams
from .request_equipment_withdraw import request_equipment_withdraw
from .request_reel_withdraw import request_reel_withdraw

def data_tech_withdraw_material():
    ''' #actualizamos y registramos los materiales de tecnico y del almacen
    assign_materials() '''
    #retira los equipos al tecnico
    #assign_teams()
    
    #traemos los una lista de id, un boleano de el equipo devuelto
    serial = request_equipment_withdraw(session.get('technical_equipments'))
    #traemos los una lista de id, un boleano de la carreta devuelta
    reel = request_reel_withdraw(session.get('technical_reels'))
    
    #actualizamos los materiales del tecnico y del almacen


    json = dict()
    json['serials'] = serial
    json['reel'] = reel
    return json