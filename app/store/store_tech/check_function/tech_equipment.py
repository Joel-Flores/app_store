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