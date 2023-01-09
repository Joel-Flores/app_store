from flask import redirect, url_for
from app.db import get_db

from .new_serial import new_serial
from app.auth.user_data import data_user
def logic_new_serial():
    #agregamos los equipos al almacen
    new_serial()
    #actulaziar los datos del almacen
    data_user()
    return redirect(url_for('store.index'))

def get_new_serial():
    db, c = get_db()
    c.execute('SELECT id, name_model FROM model_equipments WHERE id !=1;')
    return c.fetchall()