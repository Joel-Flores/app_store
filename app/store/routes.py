#importar la configurcion del blueprint
from . import store

#importacion de herramientas de flask
from flask import request, render_template, redirect, url_for

#datos basicos del usuario
from app.auth.user_data import data_user
#funcion para la ruta de index
from .index import logic_index

'''funciones para las rutas, para una accion para el tecnico'''
from .check_function import logic_check_function
#agrega materiales, equipos, carretas al tecnico 
from .tech_new_material import logic_tech_new_material
#retira los materiales del tecnico 
from .tech_withdraw_material.data_tech_withdraw_material import data_tech_withdraw_material

'''funciones para las rutas de agregar al almacen'''
#agregar materiales al almacen
from .new_material import logic_new_material
#agregar equipos al almacen
from .new_serial import logic_new_serial
from .new_serial.data_form_new_equipment import data_form_new_equipment
#agregar carretas al almacen
from .new_reel.data_new_reel import data_new_reel


"""
pagina pricipal del almacen"""
@store.route('/')
def index():
    return logic_index()

"""
rutas para asignasion de materiales y series a los tecnicos
    agregar-retirar-revisar material, revisar ots """
@store.route('/check_function', methods = ['POST'])
def check_function():
    return logic_check_function()
    
#agregar material al tecnico
@store.route('/tech_new_material', methods = ['GET','POST'])
def tech_new_material():
    if request.method == 'POST':
        return logic_tech_new_material()
    return render_template('/store/form_for_tech/tech_new_material_form.html')

#retirar material al tecnico
@store.route('/tech_withdraw_material', methods = ['GET','POST'])
def tech_withdraw_material():
    if request.method == 'POST':
        json = data_tech_withdraw_material()
        return json
        ''' #actulaziar los datos del almacen
        data_user()
        return redirect(url_for('store.index')) '''
    return render_template('/store/form_for_tech/tech_withdraw_material_form.html')

#revisar material del tecnico
@store.route('/tech_check_material')
def tech_check_material():
    return 'traer todos los materiales que tiene el tecnico'

#revisar ordenes ejecutadas del tecnico
@store.route('/store/tech_check_orders')
def tech_check_orders():
    return 'traer las ordenes no revisadas del tecnico'

"""
rutas para ingresar materiales, equipos, carretas a almacen
"""
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
    json = data_form_new_equipment()
    return render_template('/store/forms_for_update_store/form_new_equipment.html', equipments = json)

#ingresar nuevas carretas a almacen
@store.route('/new_reel', methods = ['GET','POST'])
def new_reel():
    if request.method == 'POST':
        #agregamos los equipos al almacen
        data_new_reel()
        ##actulaziar los datos del almacen
        data_user()
        return redirect(url_for('store.index'))
    return render_template('/store/forms_for_update_store/form_new_reel.html')