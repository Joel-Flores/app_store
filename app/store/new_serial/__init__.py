from flask import redirect, url_for
from .new_serial import data_new_serial
from app.auth.user_data import data_user
def logic_new_serial():
    #agregamos los equipos al almacen
    data_new_serial()
    #actulaziar los datos del almacen
    data_user()
    return redirect(url_for('store.index'))