from flask import g, session
from app.db import get_db


# traer materiales asignados al usuario
def data_materials(user_id):
    db, c = get_db()
    query = '''SELECT m.id, m.cable_hdmi,
    m.cable_rca,
    m.spliter_two,
    m.spliter_three,
    m.remote_control,
    m.connector_int,
    m.connector_ext,
    m.power_supply,
    m.q_span,
    m.cp_black,
    m.sp_black,
    m.sp_withe,
    m.satellite_dish,
    m.lnb
    FROM material_assignment AS ma
    INNER JOIN materials AS m ON ma.material_id = m.id
    WHERE ma.user_id = %s AND ma.register_active = true;
    '''
    c.execute(query,[user_id])
    return c.fetchone()

#traer la cantidad de equipos que tiene el usuario
def data_equipments(user_id):
    db, c = get_db()
    
    query = '''SELECT m.id, m.name_model, COUNT(*) AS count
    FROM equipment_assignment AS ea
    INNER JOIN serial_equipments AS s ON ea.serial_id = s.id
    INNER JOIN model_equipments AS m ON m.id = s.model_id
    WHERE ea.user_id = %s AND ea.register_active = true
    GROUP BY m.name_model;
    '''
    c.execute(query,[user_id])
    equipments = c.fetchall()
    return equipments

#traer equipos asignados al tecnico
def data_serials(user_id):
    db, c = get_db()
    
    query = '''SELECT s.id, s.cm_mac, m.name_model
    FROM equipment_assignment AS e
    INNER JOIN serial_equipments AS s ON e.serial_id = s.id
    INNER JOIN model_equipments AS m ON s.model_id = m.id
    WHERE e.register_active = true AND user_id = %s;
        '''
    c.execute(query,[user_id])
    serials = c.fetchone()
        
    return serials

def data_user():
    user_id = session.get('user')
    user_id = user_id['id']
    materials = data_materials(user_id)
    equipment = data_equipments(user_id)
    serials = data_serials(user_id)
    
    session['materials'] = materials
    session['serials'] = serials
    session['equipment'] = equipment