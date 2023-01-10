from app.db import get_db
from . import name_materials
from . import resquiest_form
def request_material():
    db, c = get_db()
    #traemos en una lista los nombres de los materiales
    name_material = name_materials.name_materials(c)
    #ponemos los materiales en un diccionario y una lista
    return resquiest_form.resquiest_form(name_material)