from flask import redirect, url_for

from .data_for_check_function import data_for_check_function
def logic_check_function():
    id = data_for_check_function()
    
    if id == 1:
        response = redirect(url_for('store.tech_new_material'))
    elif id == 2:
        response = redirect(url_for('store.tech_withdraw_material'))
    elif id == 3:
        response = redirect(url_for('store.tech_check_orders'))
    elif id == 4:
        response = redirect(url_for('store.tech_check_material'))
    return response