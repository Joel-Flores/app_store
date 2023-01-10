from app.db import get_db
from app.warehouse_function import search, delete, insert

def equipment(series, user_id):
    message = list()
    db, c = get_db()
    error = False
    for serie in series:
        #buscar id de la serie
        equipment = search.id_equipment(c, serie)
        #consultamos si hay registro en el almacen
        if equipment is None:
            message.append(f'equipo {serie} no registrado en almacen')
            error = True
        else:
            #eliminamos el registro del almacen
            delete.equipments(db, c, equipment['id'])
            #agregamos el registro de que se envio a tigo
            insert.equipment(db, c, user_id, equipment['id'], user_id, 2)
            #eliminamos el equipo del almacen
            delete.equipments_serial(db, c, equipment['id'])
    if error is False:
        message.append('equipos eliminados de almacen')
        message.append('equipos registrados en el almacen tigo')
    return message