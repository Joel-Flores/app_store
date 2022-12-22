def update_equipment_store(db, c, user_id, serials_id):
    query = 'INSERT INTO equipment_assignment (user_id, serial_id) VALUES (%s, %s);'
    for serial in serials_id:
        values = [user_id, serial['id']]
        c.execute(query, values)
        db.commit()