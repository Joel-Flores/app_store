from flask import g, session
from app.db import get_db
from .materials import data_materials
from .equipments import data_count_equipments, data_serials_equipments
from .reels import data_count_reel, data_series_reel

def data_user():
    db, c = get_db()
    user = session.get('user')
    session.clear()
    
    user_id = user['id']
    session['user'] = user
    session['materials'] = data_materials(c, user_id)
    session['equipment_count'] = data_count_equipments(c, user_id)
    session['equipment_serials'] = data_serials_equipments(c, user_id)
    session['reel_count'] = data_count_reel(c, user_id)
    session['reel_series'] = data_series_reel(c, user_id)