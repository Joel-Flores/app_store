from flask import request, session, redirect, url_for
from . import data
from app.auth.user_data import data_user
from app.store.store_tech.check_function.tech_name import tech_name
def logic_invoice():
    user = session.get('user')
    tech_id = int(request.form['id_technical'])
    series = request.form['series'].split("\r\n")
    
    message = data.equipment(series, user['id'], tech_id)
    data_user()
    response = redirect(url_for('store.index'))
    return response, message