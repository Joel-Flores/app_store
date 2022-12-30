from flask import g, session
from app.db import get_db

from app.store.for_request_material.for_request_material import for_request_material
from app.store.register_material.register_material import register_material
from app.store.register_material.update_material import update_material

def data_new_material():
    db, c = get_db()
    #traemos en una lista los nombres de los materiales
    material_dict, material_list = for_request_material()
    #registramos los materiales al almacen y actualizamos sus materiales sumandolos
    register_material(db, c, material_list, 1, g.user['id'], None)
    update_material(db, c, material_dict,  session.get('materials'))