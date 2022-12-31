from flask import redirect, url_for

from .data_new_material import data_new_material
from app.auth.user_data import data_user
def logic_new_material():
    data_new_material()
    data_user()
    return redirect(url_for('store.index'))