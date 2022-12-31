def data_count_equipments(c, user_id):
    query = '''SELECT m.id, m.name_model, COUNT(*) AS count
    FROM equipments_store AS es
    INNER JOIN equipments_serial AS s ON es.serial_id = s.id
    INNER JOIN model_equipments AS m ON m.id = s.model_id
    WHERE es.user_id = %s AND es.status_id = 1 AND es.register_active = true
    GROUP BY m.id;
    '''
    c.execute(query,[user_id])
    return c.fetchall()

def data_serials_equipments(c, user_id):   
    query = '''SELECT e.id, s.cm_mac, m.name_model
    FROM equipments_store AS e
    INNER JOIN equipments_serial AS s ON e.serial_id = s.id
    INNER JOIN model_equipments AS m ON s.model_id = m.id
    WHERE e.register_active = True AND status_id = 1 AND user_id = %s
    ORDER BY m.name_model;
    '''
    c.execute(query,[user_id])
    return c.fetchall()