from flask import redirect, url_for, flash, request
from .data_post import data_tech_all
def post_check_function():
    try:
        id = int(request.form['type_function'])
        
    except:
        id = None
        
    if id is None:
        flash('No seleccionaste un opcion.')
        return redirect(url_for('store.index'))
    
    if id == 1:
        response = redirect(url_for('store.tech_new_material'))
        
    elif id == 2:
        response = redirect(url_for('store.tech_withdraw_material'))
        
    elif id == 3:
        response = redirect(url_for('store.tech_check_all'))
        
    elif id == 4:
        response = redirect(url_for('store.tech_check_orders'))
    
    data_tech_all()
    return response