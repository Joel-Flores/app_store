from flask import g, session, flash
from app.db import get_db

from app.for_request_material import request_material
from app.warehouse_function import register, update, insert
def new_material():
    user_id = g.user['id']
    db, c = get_db()
    #traemos en una lista los nombres de los materiales
    material_dict, material_list = request_material()
    #registramos los materiales
    material_id = register.material(db, c, material_list, user_id)
    flash('materiales registrados')
    #actualizamos materiales del almacen sumandolos
    error = update.update_tech_store(db, c, material_dict, session.get('materials'), True)
    if error is False:
        flash('materiales del almacen actualizados')
        insert.material(db, c, user_id, material_id['id'], user_id, 1)
    else:
        flash('no se registro al almacen, error las las cantidades asignadas')