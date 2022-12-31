from flask import g, session
from app.db import get_db

from app.store.for_request_material import request_material
from .update_store_material import update_store_material
from app.store.register_material.register_material import register_material
from app.store.register_material.update_material import update_material

def assign_materials():
    db, c = get_db()
    #mandamos a traer los materiales a un paquete especifico para esta funcion
    material_dict, material_list = request_material()
    #descontamos los materiales del almacen y verificamos que no tenga error de que no tenga materiales
    error = update_store_material(db, c, material_dict)
    if error is False:
        #registramos los materiales al tecnico y actualizamos sus materiales sumandolos
        register_material(db, c, material_list, 2, g.user['id'], session.get('technical_name'))
        update_material(db, c, material_dict, session.get('technical_materials'))