#importamos las herramientas necesarias
from app.db import get_db
from flask import flash
from .request_equipment import request_equipment
from app.warehouse_function import delete, insert

def assign_teams(user_id, tech, tech_equipment):
    db, c = get_db()
    #mandamos los equipos del tecnico, cuales equipos devolivio
    options = request_equipment(tech_equipment)
    for option in options:
        #preguntamos que equipos devolvieron
        if option['bool'] is False:
            #eliminamos los registros de signacion al tecnico
            delete.equipments(db, c, option['id'])
            #agregamos al registro que devolio el equipo
            insert.equipment(db, c, user_id, option['id'], tech['id'], 4)
    flash('equipos devuletos a almacen')