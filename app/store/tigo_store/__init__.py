#importar la configurcion del blueprint
from app.store import store

#importacion de herramientas de flask
from flask import request, render_template, flash
from app.auth.routes import login_required
from app.store.routes import requeriment

'''funciones para las rutas de agregar al almacen'''
#agregar materiales al almacen
from .new_material import logic_new_material
#agregar equipos al almacen
from .new_serial import logic_new_serial, get_new_serial
#agregar carretas al almacen
from .new_reel import logic_new_reel

def message_in_flash(messages):
    for message in messages:
        flash(message)

"""
rutas para ingresar materiales, equipos, carretas a almacen"""
#ingresar nuevos materiales al almacen
@store.route('/new_material', methods = ['GET','POST'])
@login_required
def new_material():
    requeriment()
    if request.method == 'POST':
        response, messages = logic_new_material()
        message_in_flash(messages)
        return response
    return render_template('/store/tigo_store/form_new_material.html')

#ingresar nuevos equipos al sistema de almacen
@store.route('/new_serial', methods = ['GET','POST'])
@login_required
def new_serial():
    requeriment()
    if request.method == 'POST':
        response, messages = logic_new_serial()
        message_in_flash(messages)
        return response
    #traemos los nombres de los equipos
    return render_template('/store/tigo_store/form_new_equipment.html', equipments = get_new_serial())

#ingresar nuevas carretas a almacen
@store.route('/new_reel', methods = ['GET','POST'])
@login_required
def new_reel():
    requeriment()
    if request.method == 'POST':
        response, messages = logic_new_reel()
        message_in_flash(messages)
        return response
    return render_template('/store/tigo_store/form_new_reel.html')