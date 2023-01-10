#importar la configurcion del blueprint
from app.store import store

#importacion de herramientas de flask
from flask import request, render_template, flash

def message_in_flash(messages):
    for message in messages:
        flash(message)

#ruta de retirado de materiales del almacen a tigo      
@store.route('/withdraw_material', methods = ['GET','POST'])
def material_store():
    if request.method == 'POST':
        response, messages = ''
        message_in_flash(messages)
        return response
    return render_template('/store/store_tigo/form_withdraw_material.html')