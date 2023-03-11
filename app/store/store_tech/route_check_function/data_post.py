from flask import request, session, abort
from app.db import get_db

def tech_name(id, technicals):
    name_technical = None
    for technical in technicals:
        if technical['id'] == id:
            name_technical = technical 
    
    if name_technical is None:
        abort(404)
        
    return name_technical

def tech_material(c, tech_id):
    query = '''SELECT m.id, m.cable_hdmi, m.cable_rca, m.spliter_two, m.spliter_three, m.remote_control,
    m.connector_int, m.connector_ext, m.power_supply, m.q_span, m.cp_black, m.sp_black, m.sp_withe, m.satellite_dish, m.lnb
    FROM material_store_and_tech AS mt
    INNER JOIN materials AS m ON m.id = mt.material_id
    WHERE mt.user_id = %s AND mt.register_active = true;
    '''
    values = [tech_id]
    c.execute(query, values)
    return c.fetchone()

def tech_equipment(c, tech_id):
    query = '''SELECT s.id, s.cm_mac, s.cm_mac_two, s.card_number, m.name_model
    FROM equipments_assignment AS ea
    INNER JOIN equipments_serial AS s ON s.id = ea.serial_id
    INNER JOIN equipments_model AS m ON m.id = s.model_id
    WHERE ea.user_id = %s AND ea.register_active = True AND ea.status_id = 3 ORDER BY m.name_model ASC;
    '''
    values = [tech_id]
    c.execute(query, values)
    return c.fetchall()

def tech_reel(c, tech_id):
    query = '''SELECT c.id, c.serial
    FROM reel_assignment AS ca
    INNER JOIN cable_reel AS c ON c.id = ca.reel_id
    WHERE ca.user_id = %s AND ca.register_active = True AND ca.status_id = 3;
    '''
    values = [tech_id]
    c.execute(query, values)
    return c.fetchall()

def data_tech_all():
    db, c = get_db()
    try:
        tech_id = int(request.form['id_technical'])

    except:
        tech_id = None
    
    if tech_id is None:
        abort(404)
        
    session['technical_name'] = tech_name(tech_id, session.get('technical_active'))
    session['technical_materials'] = tech_material(c, tech_id)
    session['technical_equipments'] = tech_equipment(c, tech_id)
    session['technical_reels'] = tech_reel(c, tech_id)
