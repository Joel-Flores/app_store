from flask import redirect, url_for
from app.db import get_db

from . import new_serial
from app.auth.user_data import data_user
def logic_new_serial():
    #agregamos los equipos al almacen
    messages = new_serial.data_new_serial()
    #actulaziar los datos del almacen
    data_user()
    response = redirect(url_for('store.index'))
    return response, messages

def get_new_serial():
    db, c = get_db()
    c.execute('SELECT id, name_model FROM equipments_model WHERE id !=1;')
    return c.fetchall()