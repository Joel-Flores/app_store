from flask import request, session, flash
from app.db import get_db
from app.warehouse_function import search, delete, insert

def _request_form():
    seires = request.form['series'].split("\r\n")
    user = session.get('user')
    return seires, user['id']
    
def send_equipment():
    db, c = get_db()
    series, user_id = _request_form()
    error = False
    for serie in series:
        #buscar id de la serie
        equipment = search.id_equipment(c, serie)
        #consultamos si hay registro en el almacen
        if equipment is None:
            flash(f'equipo {serie} no registrado en almacen')
            error = True
        else:
            #agregamos el registro de que se envio a tigo
            insert.equipment(db, c, user_id, equipment['id'], user_id, 2)
            #eliminamos el registro del almacen
            delete.equipments(db, c, equipment['id'])
            #eliminamos el equipo del almacen
            delete.equipments_serial(db, c, equipment['id'])
    if error is False:
        flash('equipos eliminados de almacen')
        flash('equipos registrados en el almacen tigo')
