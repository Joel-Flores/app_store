#importamos las herramientas necesarias
from app.db import get_db
from flask import flash

from app.warehouse_function import insert, search, insert_store, deactivate
def assign_teams(equipments, tech, user_id):
    db, c = get_db()
    error = False
    for equipment in equipments:
        #buscar id de la serie
        equipment_id = search.id_equipment(c, equipment)
        #consultamos si hay registro en el almacen
        if equipment_id is None:
            flash(f'equipo {equipment} no registrado en almacen')
            error = True
        else:
            #eliminamos el registro del almacen
            deactivate.equipments_store(db, c, equipment_id['id'])
            insert_store.equipment(db, c, user_id, equipment_id['id'], 3)
            #agregamos la serie al tecnico
            insert.equipment(db, c, tech['id'], equipment_id['id'], user_id, 3)
    if error is False:
        flash('equipos asignados al tecnico') 