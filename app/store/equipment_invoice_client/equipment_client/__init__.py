from flask import request, session, redirect, url_for
from . import data
from app.auth.user_data import data_user
def logic_client():
    user = session.get('user')
    series = request.form['series'].split("\r\n")
    message = data.equipment(series, user['id'])
    data_user()
    response = redirect(url_for('store.index'))
    return response, message