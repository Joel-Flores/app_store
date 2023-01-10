from flask import redirect, url_for, session, request

from . import data_equipment
from app.auth.user_data import data_user
def logic_withdraw_equipment():
    user = session.get('user')
    messages = data_equipment.equipment(request.form['series'].split("\r\n"), user['id'])
    data_user()
    response = redirect(url_for('store.index'))
    return response, messages