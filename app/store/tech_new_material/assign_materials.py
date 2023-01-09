from flask import flash
from app.db import get_db

from app.for_request_material import request_material
from app.warehouse_function import insert, register, update, insert_store

def assign_materials(material_user, user_id, material_tech, tech):
    db, c = get_db()
    #mandamos a traer los materiales a un paquete especifico para esta funcion
    material_dict, material_list = request_material()
    #registramos los materiales
    material = register.material(db, c, material_list, user_id)
    #descontamos los materiales del almacen
    error = update.update_tech_store(db, c, material_dict, material_user, False)
    if error is False:
        insert_store.material(db, c, user_id, material['id'], 3)
        #actualizamos materiales del technico
        error = update.update_tech_store(db, c, material_dict, material_tech, True)
        if error is False:
            insert.material(db, c, tech['id'], material['id'], user_id, 3)
            flash('materiales asignado correctamente')
        else:
            flash('no se registro al tecnico, error las las cantidades digitadas')
    else:
        flash('no se registro al almacen, error las las cantidades digitadas')