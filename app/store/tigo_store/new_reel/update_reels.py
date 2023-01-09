from flask import flash
from app.warehouse_function import register, insert, update

def update_reels(db, c, reels, user_id):
    error = False
    
    for reel in reels:
        #traemos datos del sistema para no repetir series
        query = 'SELECT * FROM cable_reel WHERE serial = %s;'
        values = [reel]
        c.execute(query, values)
        data = c.fetchone()
        #controlamos si la serie ya esta registrada
        if data is not None:
            update.reel(db, c, data['id'])
            flash(f'la carreta con la serie: {reel}, ya esta registrado')
            error = True
        else:
            #ingresar carretas al sistema
            reel_id = register.reel(db, c, reel, user_id)
            #asignamos la carretas al almacen
            insert.reel(db, c, user_id, reel_id['id'],user_id, 1)
    return error