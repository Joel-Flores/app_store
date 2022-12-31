from flask import g, session, flash
from app.db import get_db

from app.store.for_request_material import request_material
from app.store.register_material.register_material import register_material
from app.store.register_material.update_material import update_material
from app.store.warehouse_function import register, update, insert_store
def data_new_material():
    db, c = get_db()
    #traemos en una lista los nombres de los materiales
    material_dict, material_list = request_material()
    ''' #registramos los materiales al almacen y actualizamos sus materiales sumandolos
    register_material(db, c, material_list, 1, g.user['id'], None)
    update_material(db, c, material_dict,  session.get('materials')) '''
    
    material_id = register.material(db, c, material_list, g.user['id'])
    flash('materiales registrados en el registro historico')
    update.update_tech_store(db, c, material_dict, session.get('materials'), True)
    flash('materiales del alamcen actualizados')
    insert_store.material(db, c, g.user['id'], material_id['id'], 1)
    flash('materiales registrado en el historial del alamcen')