#importar la configurcion del blueprint
from app.store import store

#importacion de herramientas de flask
from flask import request, render_template, flash

from .withdraw_material import logic_withdraw_material
from .withdraw_equipment import logic_withdraw_equipment

def message_in_flash(messages):
    for message in messages:
        flash(message)

#ruta de retirado de materiales del almacen a tigo      
@store.route('/withdraw_material', methods = ['GET','POST'])
def withdraw_material():
    if request.method == 'POST':
        response, messages = logic_withdraw_material()
        message_in_flash(messages)
        return response
    return render_template('/store/store_tigo/form_withdraw_material.html')

#ruta de retirado de equipos del almacen a tigo
@store.route('/withdraw_equipment', methods = ['GET','POST'])
def withdraw_equipment():
    if request.method == 'POST':
        response, messages = logic_withdraw_equipment()
        message_in_flash(messages)
        return response
    return render_template('/store/store_tigo/form_withdraw_equipment.html')