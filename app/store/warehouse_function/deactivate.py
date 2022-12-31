def equipments_store(db, c, serial_id):
    query = 'UPDATE equipments_store SET register_active = False WHERE serial_id = %s;'
    values = [serial_id]
    c.execute(query, values)
    db.commit()

def reel_store(db, c, reel_id):
    query = 'UPDATE cable_reel_store SET register_active = False WHERE reel_id = %s;'
    values = [reel_id]
    c.execute(query, values)
    db.commit()
    
def equipments_tech(db, c, serial_id):
    query = 'UPDATE equipments_tech SET register_active = False WHERE serial_id = %s;'
    values = [serial_id]
    c.execute(query, values)
    db.commit()

def reel_tech(db, c, reel_id):
    query = 'UPDATE cable_reel_tech SET register_active = False WHERE reel_id = %;'
    values = [reel_id]
    c.execute(query, values)
    db.commit()
    
def equipments_serial(db, c, serial_id):
    query = 'UPDATE equipments_serial SET register_active = False WHERE id = %s;'
    values = [serial_id]
    c.execute(query, values)
    db.commit()

def cable_reel(db, c, reel_id):
    query = 'UPDATE cable_reel SET register_active = False WHERE id = %s;'
    values = [reel_id]
    c.execute(query, values)
    db.commit()