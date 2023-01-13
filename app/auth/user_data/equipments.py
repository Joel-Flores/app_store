def data_count_equipments(c, user_id):
    query = '''SELECT m.id, m.name_model, COUNT(*) AS count
    FROM equipments_assignment AS ea
    INNER JOIN equipments_serial AS s ON ea.serial_id = s.id
    INNER JOIN equipments_model AS m ON m.id = s.model_id
    WHERE ea.user_id = %s AND ea.register_active = true
    GROUP BY m.id;
    '''
    c.execute(query,[user_id])
    return c.fetchall()

def data_serials_equipments(c, user_id):   
    query = '''SELECT e.id, s.cm_mac, m.name_model
    FROM equipments_assignment AS e
    INNER JOIN equipments_serial AS s ON e.serial_id = s.id
    INNER JOIN equipments_model AS m ON s.model_id = m.id
    WHERE e.register_active = True AND user_id = %s
    ORDER BY m.name_model;
    '''
    c.execute(query,[user_id])
    return c.fetchall()