from flask import render_template, redirect, url_for
from .data_post import withdraw_material
from app.auth.user_data import data_user

def post_withdraw_material():
    withdraw_material()
    #actulaziar los datos del almacen
    data_user()
    return redirect(url_for('store.index'))

def get_withdraw_material():
    return render_template('/store/store_tech/tech_withdraw_material_form.html')