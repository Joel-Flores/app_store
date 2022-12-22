#importar la configurcion del blueprint
from . import store

#importacion de herramientas de flask
from flask import request, render_template, redirect, url_for

#datos basicos del usuario
from app.auth.user_data import data_user
#funcion para la ruta de index
from .index.data_for_index import data_for_index

'''funciones para las rutas, para una accion para el tecnico'''
#redireciona a una acion especifica
from .check_function.data_for_check_function import data_for_check_function
#agrega materiales, equipos, carretas al tecnico 
from .tech_new_material.data_tech_new_material import data_tech_new_material

'''funciones para las rutas de agregar al almacen'''
#agregar materiales al almacen
from .new_material.data_new_material import data_new_material

from .new_serial.data_form_new_equipment import data_form_new_equipment


"""
pagina pricipal del almacen
"""
@store.route('/')
def index():
    data_for_index()
    return render_template('/store/index.html')

"""
rutas para asignasion de materiales y series a los tecnicos
    agregar-retirar-revisar material, revisar ots 
"""
@store.route('/check_function', methods = ['POST'])
def check_function():
    id = data_for_check_function()
    if id == 1:
        return redirect(url_for('store.tech_new_material'))
    elif id == 2:
        return redirect(url_for('store.tech_withdraw_material'))
    elif id == 3:
        return redirect(url_for('store.tech_check_orders'))
    elif id == 4:
        return redirect(url_for('store.tech_check_material'))
    
#agregar material al tecnico
@store.route('/tech_new_material', methods = ['GET','POST'])
def tech_new_material():
    if request.method == 'POST':
        data_tech_new_material()
        #actulaziar los datos del almacen
        data_user()
        return redirect(url_for('store.index'))
    return render_template('/store/form_for_tech/tech_new_material_form.html')

#retirar material al tecnico
@store.route('/tech_withdraw_material', methods = ['GET','POST'])
def tech_withdraw_material():
    return 'renderizar formulario para retirar materiales'

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
        data_new_material()
        data_user()
        return redirect(url_for('store.index'))
    
    return render_template('/store/forms/form_new_material.html')

"""
ingresar nuevos equipos al sistema de almacen
"""
@store.route('/new_serial', methods = ['GET','POST'])
def new_serial():
    if request.method == 'POST':
        #actulaziar los datos del almacen
        data_user()
        return redirect(url_for('store.index'))
    json = data_form_new_equipment()
    return render_template('/store/forms/form_new_equipment.html', equipments = json)