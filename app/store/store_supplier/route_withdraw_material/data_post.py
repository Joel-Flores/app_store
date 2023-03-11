from flask import flash, session
from app.db import get_db
from app.for_request_material import request_material
from app.warehouse_function import insert, register, update

def send_material():
    db, c = get_db()
    user_id = session.get('user')
    user_id = user_id['id']
    material_user = session.get('materials')
    #mandamos a traer los materiales a un paquete especifico para esta funcion
    material_dict, material_list = request_material()
    #registramos los materiales
    material = register.material(db, c, material_list, user_id)
    #descontamos los materiales del almacen
    error = update.update_tech_store(db, c, material_dict, material_user, False)
    if error is False:
        insert.material(db, c, user_id, material['id'], user_id, 2)
        flash('materiales asignado a tigo correctamente')
    else:
        flash('no se registro al tecnico, error las las cantidades digitadas')