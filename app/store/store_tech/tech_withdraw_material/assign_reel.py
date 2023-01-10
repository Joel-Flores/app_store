#importamos las herramientas necesarias
from app.db import get_db
from flask import flash
from .request_reel_withdraw import request_reel_withdraw
from app.warehouse_function import delete, insert

def assign_reel(user_id, tech, tech_reel):
    message = list()
    db, c = get_db()
    #mandamos los equipos del tecnico, cuales equipos devolivio
    options = request_reel_withdraw(tech_reel)
    for option in options:
        #preguntamos que equipos devolvieron
        if option['bool'] is not False:
            #eliminamos los registros de signacion al tecnico
            delete.reel(db, c, option['id'])
            #eliminamos la carreta del registro del almacen
            delete.cable_reel(db, c, option['id'])
            #agregamos al registro que devolio el equipo
            insert.reel(db, c, user_id, option['id'], tech['id'], 8)
    message.append('carretas devuletas a almacen')
    return message