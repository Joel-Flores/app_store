from flask import g, session
from app.db import get_db
from .materials import data_materials
from .equipments import data_count_equipments, data_serials_equipments
from .reels import data_count_reel, data_series_reel

def data_user():
    db, c = get_db()
    user_id = session.get('user')
    user_id = user_id['id']
    material = data_materials(c, user_id)
    equipment_count = data_count_equipments(c, user_id)
    equipment_serials = data_serials_equipments(c, user_id)
    reel_count = data_count_reel(c, user_id)
    reel_series = data_series_reel(c, user_id)
        
    session['materials'] = material
    session['equipment_count'] = equipment_count
    session['equipment_serials'] = equipment_serials
    session['reel_count'] = reel_count
    session['reel_series'] = reel_series