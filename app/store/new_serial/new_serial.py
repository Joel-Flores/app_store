from flask import g, flash, request
from app.db import get_db

from .update_equipment import update_equipment
from .update_equipment_store import update_equipment_store
def data_new_serial():
    db, c = get_db()
    user_id = g.user['id']
    
    #sube los equipos al sistema y nos trae los id del registro
    serials_id, error = update_equipment(db, c, user_id)
    if error is False:
        #asignando los equipos al almacen
        update_equipment_store(db, c, user_id, serials_id)
        flash('Equipos Subidos')
    else:
        flash('error al ingresar las series')
