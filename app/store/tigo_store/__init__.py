#importar la configurcion del blueprint
from . import store

#importacion de herramientas de flask
from flask import request, render_template

'''funciones para las rutas de agregar al almacen'''
#agregar materiales al almacen
from tigo_store.new_material import logic_new_material
#agregar equipos al almacen
from tigo_store.new_serial import logic_new_serial, get_new_serial
#agregar carretas al almacen
from tigo_store.new_reel import logic_new_reel

"""
rutas para ingresar materiales, equipos, carretas a almacen"""
#ingresar nuevos materiales al almacen
@store.route('/new_material', methods = ['GET','POST'])
def new_material():
    if request.method == 'POST':
        return logic_new_material()
    return render_template('/store/forms_for_update_store/form_new_material.html')

#ingresar nuevos equipos al sistema de almacen
@store.route('/new_serial', methods = ['GET','POST'])
def new_serial():
    if request.method == 'POST':
        return logic_new_serial()
    #traemos los nombres de los equipos
    return render_template('/store/forms_for_update_store/form_new_equipment.html', equipments = get_new_serial())

#ingresar nuevas carretas a almacen
@store.route('/new_reel', methods = ['GET','POST'])
def new_reel():
    if request.method == 'POST':
        return logic_new_reel()
    return render_template('/store/forms_for_update_store/form_new_reel.html')