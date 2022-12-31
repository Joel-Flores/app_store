def equipment(db, c, user_id, serial_id, status_id):
    query = 'INSERT INTO equipments_store(user_id, serial_id, status_id) VALUES(%s, %s, %s);'
    values = [user_id, serial_id, status_id]
    c.execute(query, values)
    db.commit()

def material(db, c, user_id, material_id, status_id):
    query = 'INSERT INTO material_store_assignment(user_id, material_id, status_id) VALUES(%s, %s, %s);'
    values = [user_id, material_id, status_id]
    c.execute(query, values)
    db.commit()

def reel(db, c, user_id, reel_id, status_id):
    query = 'INSERT INTO cable_reel_store(user_id, reel_id, status_id) VALUES(%s, %s, %s);'
    values = [user_id, reel_id, status_id]
    c.execute(query, values)
    db.commit()

def invoiced (db, c, user_id, serial_id, code_id, status_id):
    query = 'INSERT INTO equipments_invoiced(user_id, serial_id, code_id, status_id) VALUES(%s, %s, %s, %s);'
    values = [user_id, serial_id, code_id, status_id]
    c.execute(query, values)
    db.commit()