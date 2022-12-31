from flask import redirect, url_for, session

from .data_for_check_function import data_for_check_function
def logic_check_function():
    id = data_for_check_function()
    #sacamos la version json del la consulta
    json = dict()
    json['technical_name'] = session.get('technical_name')
    json['technical_materials'] = session.get('technical_materials')
    #return json
    if id == 1:
        return redirect(url_for('store.tech_new_material'))
    elif id == 2:
        return redirect(url_for('store.tech_withdraw_material'))
    elif id == 3:
        return redirect(url_for('store.tech_check_orders'))
    elif id == 4:
        return redirect(url_for('store.tech_check_material'))