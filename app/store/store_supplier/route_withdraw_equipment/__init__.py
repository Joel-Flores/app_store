from flask import render_template, redirect, url_for
from .data_post import send_equipment
from app.auth.user_data import data_user

def post_withdraw_equipment():
    send_equipment()
    data_user()
    return redirect(url_for('store.index'))

def get_withdraw_equipment():
    return render_template('/store/store_tigo/form_withdraw_equipment.html')