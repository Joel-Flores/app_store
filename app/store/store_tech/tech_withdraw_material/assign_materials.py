from flask import flash
from app.db import get_db

from app.for_request_material import request_material
from app.warehouse_function import insert, register,insert_store, update

def assign_materials(user_id, material_user, tech, material_tech):
    db, c = get_db()
    #mandamos a traer los materiales a un paquete especifico para esta funcion
    material_dict, material_list = request_material()
    #registramos los materiales
    material = register.material(db, c, material_list, user_id)
    #descontamos los materiales del tecnico
    error = update.update_tech_store(db, c, material_dict, material_tech, False)
    if error is False:
        #actualizamos materiales del almacen
        error = update.update_tech_store(db, c, material_dict, material_user, True)
        if error is False:
            insert.material(db, c, tech['id'], material['id'], user_id, 4)
            flash('materiales registrados')
        else:
            flash('no se registro al almacen, error las las cantidades digitadas')
    else:
        flash('no se registro al almacen, error las las cantidades digitadas')