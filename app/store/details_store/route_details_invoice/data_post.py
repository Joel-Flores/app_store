from flask import request, session, abort
from app.db import get_db
def tech_name(id, technicals):
    name_technical = None
    for technical in technicals:
        if technical['id'] == id:
            name_technical = f'{technical["user_name"]} {technical["user_lastname"]}' 
    
    if name_technical is None:
        abort(404)
        
    return name_technical

def rename_tec(values):
    for value in values:
        tech_id = value['tech_id']
        value['tech_id'] = tech_name(tech_id, session.get('technical_active'))
        
    return values

def list_equipment_invoice():
    db, c = get_db()
    tech_id = request.form['id_technical']
    query = '''SELECT e.id, s.cm_mac, s.cm_mac_two, s.card_number, m.name_model, sm.status_material, e.created_in, e.user_id as tech_id
    FROM equipments_assignment AS e
    INNER JOIN equipments_serial AS s ON e.serial_id = s.id
    INNER JOIN equipments_model AS m ON s.model_id = m.id
    INNER JOIN status_materials AS sm ON e.status_id = sm.id
    WHERE e.register_active = True AND sm.id = 10 AND e.user_id = %s
    ORDER BY sm.status_material;'''
    values = [tech_id]
    c.execute(query, values)
    response = rename_tec(c.fetchall())
    return response