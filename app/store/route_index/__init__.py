from flask import session, render_template
from app.auth.user_data import data_user

from .data_get import data_technical

def get_index():
    data_user()
    #guarda el id , nombre, apellido de los tecnicos
    session['technical_active'] = data_technical()
    return render_template('/store/index.html')