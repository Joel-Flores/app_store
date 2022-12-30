from flask import g, session
from app.db import get_db

from app.store.for_request_material.for_request_material import for_request_material
from .update_tech_material import update_tech_material
from app.store.register_material.register_material import register_material
from app.store.register_material.update_material import update_material

def assign_materials():
    db, c = get_db()
    #mandamos a traer los materiales a un paquete especifico para esta funcion
    material_dict, material_list = for_request_material()
    #descontamos los materiales del almacen y verificamos que no tenga error de que no tenga materiales
    error = update_tech_material(db, c, material_dict)
    if error is False:
        register_material(db, c, material_list, 1, g.user['id'], None)
        update_material(db, c, material_dict,  session.get('materials'))