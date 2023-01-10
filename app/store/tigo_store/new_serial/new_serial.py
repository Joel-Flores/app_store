from flask import g
from app.db import get_db

from .request_equipment import request_equipment

def data_new_serial():
    db, c = get_db()
    user_id = g.user['id']
    
    #sube los equipos al sistema y nos trae los id del registro
    error, message = request_equipment(db, c, user_id)
    if error is False:
        message.append('Equipos Subidos al Almacen')
    return message
