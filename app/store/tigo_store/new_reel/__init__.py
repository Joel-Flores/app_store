from flask import redirect, url_for

from app.store.new_reel.request_new_reel import request_new_reel
from app.auth.user_data import data_user
def logic_new_reel():
    #agregamos los equipos al almacen
        request_new_reel()
        ##actulaziar los datos del almacen
        data_user()
        return redirect(url_for('store.index'))