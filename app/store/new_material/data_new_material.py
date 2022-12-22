from app.db import get_db

from .name_materials import name_materials
from .resquiest_form import resquiest_form
from .register_material_store import register_material_store
from .update_material_store import update_material_store
def data_new_material():
    db, c = get_db()
    #traemos en una lista los nombres de los materiales
    name_material = name_materials(c)
    #ponemos los materiales en un diccionario y una lista
    material_dict, material_list = resquiest_form(name_material)
    #registramos los materiales al almacen y actualizamos sus materiales sumandolos
    register_material_store(db, c, material_list)
    update_material_store(db, c, material_dict)