from app.db import get_db
def tech_equipment(tech_id):
    db, c = get_db()
    query = '''SELECT s.id, s.cm_mac, s.cm_mac_two, s.card_number, m.name_model
    FROM equipment_assignment AS ea
    INNER JOIN serial_equipments AS s ON s.id = ea.serial_id
    INNER JOIN model_equipments AS m ON m.id = s.model_id
    WHERE ea.user_id = %s AND ea.register_active = True ORDER BY m.name_model ASC;
    '''
    values = [tech_id]
    c.execute(query, values)
    return c.fetchall()