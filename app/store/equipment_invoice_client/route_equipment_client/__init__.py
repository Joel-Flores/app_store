from flask import request, session, redirect, url_for, render_template
from .data_post import equipment
from app.auth.user_data import data_user

def post_equipment_client():
    user = session.get('user')
    series = request.form['series'].split("\r\n")
    equipment(series, user['id'])
    data_user()
    return redirect(url_for('store.index'))

def get_equipment_client():
    return render_template('/store/equipment_invoice_client/form_equipment_client.html')