from flask import request, session, redirect, url_for, render_template
from .data_post import equipment
from app.auth.user_data import data_user
#from app.store.store_tech.route_check_function.data_post import tech_name

def post_tech_invoice():
    user = session.get('user')
    tech_id = int(request.form['id_technical'])
    series = request.form['series'].split("\r\n")
    
    equipment(series, user['id'], tech_id)
    data_user()
    return redirect(url_for('store.index'))

def get_tech_invoice():
    return render_template('/store/equipment_invoice_client/form_equipment_invoice.html')