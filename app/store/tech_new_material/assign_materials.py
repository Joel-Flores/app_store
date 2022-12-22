from app.db import get_db

from .name_materials import name_materials
from .resquiest_form import resquiest_form
from .update_store_material import update_store_material
from .register_material_tech import register_material_tech
from .update_material_tech import update_material_tech

def assign_materials():
    db, c = get_db()
    name_material = name_materials(c)
    material_dict, material_list = resquiest_form(name_material)
    error = update_store_material(db, c, material_dict)
    if error is False:
        register_material_tech(db, c, material_list)
        update_material_tech(db, c, material_dict)