from flask import render_template, redirect, url_for
from app.auth.user_data import data_user
from .data_post import new_serial
from .data_get import model_equipment

def post_new_serial():
    new_serial()
    data_user()
    return redirect(url_for('store.index'))

def get_new_serial():
    equipments = model_equipment()
    return render_template('/store/tigo_store/form_new_equipment.html', equipments = equipments)