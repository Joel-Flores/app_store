from app.db import get_db
from app.warehouse_function import search, delete, insert
def equipment(series, user_id):
    message = list()
    db, c = get_db()
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
            insert.equipment(db, c, user_id, equipment['id'], user_id, 5)
    if error is False:
        message.append('equipos agregado a la lista con cliente')
    return message