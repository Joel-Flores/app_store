#importar la configurcion del blueprint
from app.store import store

#importacion de herramientas de flask
from flask import request, render_template, flash
from app.auth.routes import login_required
from app.store.routes import requeriment

'''funciones para las rutas, para una accion para el tecnico'''
from .route_check_function import post_check_function
from .route_tech_new_material import post_tech_new_material, get_tech_new_material
from .route_tech_withdraw_material import post_withdraw_material, get_withdraw_material

def message_in_flash(messages):
    for message in messages:
        flash(message)

"""
rutas para asignasion de materiales y series a los tecnicos
    agregar-retirar-revisar material, revisar ots """
@store.route('/check_function', methods = ['POST'])
@login_required
def check_function():
    requeriment()
    return post_check_function()
    
#agregar material al tecnico
@store.route('/tech_new_material', methods = ['GET','POST'])
@login_required
def tech_new_material():
    requeriment()
    if request.method == 'POST':
        return post_tech_new_material()
    
    return get_tech_new_material()

#retirar material al tecnico
@store.route('/tech_withdraw_material', methods = ['GET','POST'])
@login_required
def tech_withdraw_material():
    requeriment()
    if request.method == 'POST':
        return post_withdraw_material()
    
    return get_withdraw_material()

#revisar equipos del tecnico "PENDIENTE"
@store.route('/tech_check_all')
@login_required
def tech_check_all():
    requeriment()
    return render_template('/store/store_tech/tech_view_all_material.html')


#revisar ordenes ejecutadas del tecnico "PENDIENTE"
@store.route('/store/tech_check_orders')
def tech_check_orders():
    requeriment()
    return 'traer las ordenes no revisadas del tecnico'