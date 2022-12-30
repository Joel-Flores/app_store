from app.db import get_db
from .name_materials import name_materials
from .resquiest_form import resquiest_form
def for_request_material():
    db, c = get_db()
    #traemos en una lista los nombres de los materiales
    name_material = name_materials(c)
    #ponemos los materiales en un diccionario y una lista
    material_dict, material_list = resquiest_form(name_material)
    return material_dict, material_list