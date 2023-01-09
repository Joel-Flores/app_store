def equipment(db, c, user_id, serial_id, registered_by, status_id):
    query = 'INSERT INTO equipments_assignment(user_id, serial_id, registered_by, status_id) VALUES(%s, %s, %s, %s);'
    values = [user_id, serial_id, registered_by, status_id]
    c.execute(query, values)
    db.commit()
    
def material(db, c, user_id, material_id, registered_by, status_id):
    query = 'INSERT INTO material_assignment(user_id, material_id, registered_by, status_id) VALUES(%s, %s, %s, %s);'
    values = [user_id, material_id, registered_by, status_id]
    c.execute(query, values)
    db.commit()

def reel(db, c, user_id, reel_id, registered_by, status_id):
    query = 'INSERT INTO reel_assignment(user_id, reel_id, registered_by, status_id) VALUES(%s, %s, %s, %s);'
    values = [user_id, reel_id, registered_by, status_id]
    c.execute(query, values)
    db.commit()