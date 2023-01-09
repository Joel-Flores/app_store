#importamos las herramientas necesarias
from app.db import get_db
from flask import flash
from .request_equipment import request_equipment
from app.warehouse_function import delete, insert, insert_store

def assign_teams(user_id, tech, tech_equipment):
    db, c = get_db()
    options = request_equipment(tech_equipment)
    for option in options:
        if option['bool'] is False:
            delete.equipments_tech(db, c, option['id'])
            insert.equipment(db, c, tech['id'], option['id'], user_id, 4)
            insert_store.equipment(db, c, user_id, option['id'], 4)