from app.db import get_db

from .name_materials import name_materials
from .resquiest_form import resquiest_form
from .update_store_material import update_store_material
from .register_material_tech import register_material_tech
from .update_material_tech import update_material_tech

def assign_materials():
    db, c = get_db()
    #traemos en una lista los nombres de los materiales
    name_material = name_materials(c)
    #ponemos los materiales en un diccionario y una lista
    material_dict, material_list = resquiest_form(name_material)
    #descontamos los materiales del almacen y verificamos que no tenga error de que no tenga materiales
    error = update_store_material(db, c, material_dict)
    if error is False:
        #registramos los materiales al tecnico y actualizamos sus materiales sumandolos
        register_material_tech(db, c, material_list)
        update_material_tech(db, c, material_dict)