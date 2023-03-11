#importar la configurcion del blueprint
from app.store import store

#importacion de herramientas de flask
from flask import request
from app.auth.routes import login_required
from app.store.routes import requeriment

from .route_withdraw_material import post_withdraw_material, get_withdraw_material
from .route_withdraw_equipment import post_withdraw_equipment, get_withdraw_equipment

#ruta de retirado de materiales del almacen a tigo      
@store.route('/withdraw_material', methods = ['GET','POST'])
@login_required
def withdraw_material():
    requeriment()
    if request.method == 'POST':
        return post_withdraw_material()
    
    return get_withdraw_material()

#ruta de retirado de equipos del almacen a tigo
@store.route('/withdraw_equipment', methods = ['GET','POST'])
@login_required
def withdraw_equipment():
    requeriment()
    if request.method == 'POST':
        return post_withdraw_equipment()
    
    return get_withdraw_equipment()