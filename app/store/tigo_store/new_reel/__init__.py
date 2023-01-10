from flask import redirect, url_for

from . import request_new_reel
from app.auth.user_data import data_user
def logic_new_reel():
    #agregamos los equipos al almacen
        messages = request_new_reel.request_new_reel()
        ##actulaziar los datos del almacen
        data_user()
        response = redirect(url_for('store.index'))
        return response, messages