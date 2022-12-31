def equipment(db, c, user_id, serial_id, status_id):
    query = 'INSERT INTO equipments_tech(user_id, serial_id, status_id) VALUES(%s, %s, %s);'
    values = [user_id, serial_id, status_id]
    c.execute(query, values)
    db.commit()
    
def material(db, c, user_id, material_id, registered_by, status_id):
    query = 'INSERT INTO material_tech_assignment(user_id, material_id, registered_by, status_id) VALUES(%s, %s, %s, %s);'
    values = [user_id, material_id, registered_by, status_id]
    c.execute(query, values)
    db.commit()

def reel(db, c, user_id, reel_id, registered_by, status_id):
    query = 'INSERT INTO cable_reel_tech(user_id, reel_id, registered_by, status_id) VALUES(%s, %s, %s, %s);'
    values = [user_id, reel_id, registered_by, status_id]
    c.execute(query, values)
    db.commit()