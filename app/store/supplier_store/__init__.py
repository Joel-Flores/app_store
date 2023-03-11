from app.store import store

from flask import request
from app.auth.routes import login_required
from app.store.routes import requeriment

from .route_new_material import post_new_material, get_new_material
from .route_new_serial import post_new_serial, get_new_serial
from .route_new_reel import post_new_reel, get_new_reel

#ingresar nuevos materiales al almacen
@store.route('/new_material', methods = ['GET','POST'])
@login_required
def new_material():
    requeriment()
    if request.method == 'POST':
        return post_new_material()
    
    return get_new_material()

#ingresar nuevos equipos al sistema de almacen
@store.route('/new_serial', methods = ['GET','POST'])
@login_required
def new_serial():
    requeriment()
    if request.method == 'POST':
        return post_new_serial()
    
    return get_new_serial()

#ingresar nuevas carretas a almacen
@store.route('/new_reel', methods = ['GET','POST'])
@login_required
def new_reel():
    requeriment()
    if request.method == 'POST':
        return post_new_reel()
    
    return get_new_reel()