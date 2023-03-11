from flask import render_template, redirect, url_for
from .data_post import send_material
from app.auth.user_data import data_user
def post_withdraw_material():
    send_material()
    data_user()
    return redirect(url_for('store.index'))

def get_withdraw_material():
    return render_template('/store/store_tigo/form_withdraw_material.html')