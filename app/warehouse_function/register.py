def equipment(db, c, values, registered_by):
    query = '''INSERT INTO equipments_serial(cm_mac,cm_mac_two,card_number, model_id, registered_by) 
    VALUES(%s, %s, %s, %s, %s);'''
    values.append(registered_by)
    c.execute(query, values)
    query = 'SELECT id FROM equipments_serial WHERE registered_by = %s ORDER BY id DESC LIMIT 1;'
    db.commit()
    values = [registered_by]
    c.execute(query, values)
    return c.fetchone()

def material(db, c, values, registered_by):
    query = '''INSERT INTO materials (cable_hdmi, cable_rca, spliter_two, spliter_three, 
    remote_control, connector_int, connector_ext, power_supply, q_span, cp_black, 
    sp_black, sp_withe, satellite_dish, lnb, registered_by) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'''
    values.append(registered_by)
    c.execute(query, values)
    db.commit()
    query = 'SELECT id FROM materials WHERE registered_by = %s ORDER BY id DESC LIMIT 1;'
    values = [registered_by]
    c.execute(query, values)
    return c.fetchone()

def reel(db, c, serial, registered_by):
    query = 'INSERT INTO cable_reel(serial, registered_by) VALUES(%s, %s);'
    values = [serial, registered_by]
    c.execute(query, values)
    db.commit()
    query = 'SELECT id FROM cable_reel WHERE registered_by = %s ORDER BY id DESC LIMIT 1;'
    values = [registered_by]
    c.execute(query, values)
    return c.fetchone()
