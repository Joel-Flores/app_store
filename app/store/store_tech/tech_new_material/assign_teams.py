#importamos las herramientas necesarias
from app.db import get_db

from app.warehouse_function import insert, search, insert, delete
def assign_teams(equipments, tech, user_id):
    message = list()
    db, c = get_db()
    error = False
    for equipment in equipments:
        #buscar id de la serie
        equipment_id = search.id_equipment(c, equipment)
        #consultamos si hay registro en el almacen
        if equipment_id is None:
            message.append(f'equipo {equipment} no registrado en almacen')
            error = True
        else:
            #eliminamos el registro del almacen
            delete.equipments(db, c, equipment_id['id'])
            #agregamos la serie al tecnico
            insert.equipment(db, c, tech['id'], equipment_id['id'], user_id, 3)
    if error is False:
        message.append('equipos asignados al tecnico')
    return message