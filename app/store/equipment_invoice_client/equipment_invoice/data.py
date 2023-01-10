from app.db import get_db
from app.warehouse_function import search, delete, insert
def equipment(series, user_id, tech_id):
    db, c = get_db()
    message = list()
    error = False
    for serie in series:
        equipment = search.id_equipment(c, serie)
        if equipment is None:
            message.append(f'equipo {serie} no registrado en almacen')
            error = True
        else:
            #eliminamos el registro del almacen
            delete.equipments(db, c, equipment['id'])
            #agregamos el registro de que se envio a tigo
            insert.equipment(db, c, tech_id, equipment['id'], user_id, 10)
            delete.equipments_serial(db, c, equipment['id'])
    if error is False:
        message.append('equipos Facturado al tecnico')
        message.append('equipos eliminado del registro')
    return message