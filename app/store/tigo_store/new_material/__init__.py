from flask import redirect, url_for

from . import data_new_material
from app.auth.user_data import data_user
def logic_new_material():
    messages = data_new_material.new_material()
    data_user()
    response = redirect(url_for('store.index'))
    return response, messages