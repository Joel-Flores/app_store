#importar la configurcion del blueprint
from app.store import store

#importacion de herramientas de flask
from flask import request, render_template, flash

'''funciones para las rutas, para una accion para el tecnico'''
from .check_function import logic_check_function
#agrega materiales, equipos, carretas al tecnico 
from .tech_new_material import logic_tech_new_material
#retira los materiales del tecnico 
from .tech_withdraw_material import logic_tech_withdraw_material

def message_in_flash(messages):
    for message in messages:
        flash(message)

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
        response, message = logic_tech_new_material()
        message_in_flash(message)
        return response
    return render_template('/store/form_for_tech/tech_new_material_form.html')

#retirar material al tecnico
@store.route('/tech_withdraw_material', methods = ['GET','POST'])
def tech_withdraw_material():
    if request.method == 'POST':
        response, message = logic_tech_withdraw_material()
        message_in_flash(message)
        return response
    return render_template('/store/form_for_tech/tech_withdraw_material_form.html')

#revisar material del tecnico
@store.route('/tech_check_material')
def tech_check_material():
    return 'traer todos los materiales que tiene el tecnico'

#revisar ordenes ejecutadas del tecnico
@store.route('/store/tech_check_orders')
def tech_check_orders():
    return 'traer las ordenes no revisadas del tecnico'