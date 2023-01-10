from flask import redirect, url_for, session
from . import data_material
from app.auth.user_data import data_user
def logic_withdraw_material():
    user = session.get('user')
    material = session.get('materials')
    messages = data_material.materials(user['id'], material)
    data_user()
    response = redirect(url_for('store.index'))
    return response, messages