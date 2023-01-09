def id_equipment (c, cm_mac):
    query = 'SELECT id FROM equipments_serial WHERE cm_mac = %s AND register_active = True;'
    values = [cm_mac]
    c.execute(query, values)
    return c.fetchone()

def id_reel (c, serial):
    query = 'SELECT id FROM cable_reel WHERE serial = %s AND register_active = True;'
    values = [serial]
    c.execute(query, values)
    return c.fetchone()

def id_code (c, serial_id):
    query = 'SELECT code_id FROM code_work_orders WHERE serial_id = %s;'
    values = [serial_id]
    c.execute(query, values)
    return c.fetchone()