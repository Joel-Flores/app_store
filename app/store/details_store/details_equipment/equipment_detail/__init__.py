def _equipment_detail(c, user_id, id_model, id_status):
    message = list()
    query = '''SELECT e.id, s.cm_mac, s.cm_mac_two, s.card_number, m.name_model, sm.status_material, e.created_in
    FROM equipments_assignment AS e
    INNER JOIN equipments_serial AS s ON e.serial_id = s.id
    INNER JOIN equipments_model AS m ON s.model_id = m.id
    INNER JOIN status_materials AS sm ON e.status_id = sm.id
    WHERE e.register_active = True AND user_id = %s AND s.model_id = %s AND sm.id = %s
    ORDER BY sm.status_material;
    '''
    values = [user_id, id_model, id_status]
    c.execute(query, values)
    message.append('Equipos del modelo seleccionado, filtrado')
    return message, c.fetchall()