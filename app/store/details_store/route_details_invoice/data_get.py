from app.db import get_db

def list_invoice_tech_all():    
    db, c = get_db()
    query = '''SELECT e.id, s.cm_mac, s.cm_mac_two, s.card_number, m.name_model, sm.status_material, e.created_in, u.username as tech_id
    FROM equipments_assignment AS e
    LEFT JOIN user AS u ON e.user_id = u.id
    INNER JOIN equipments_serial AS s ON e.serial_id = s.id
    INNER JOIN equipments_model AS m ON s.model_id = m.id
    INNER JOIN status_materials AS sm ON e.status_id = sm.id
    WHERE e.register_active = True AND sm.id = 10
    ORDER BY sm.status_material;'''
    c.execute(query)
    return c.fetchall()