from flask import request, flash

def update_store_reel(db, c, reels, user_id):
    reel_id = list()
    for reel in reels:
        #traemos el id de registro en el almacen y el id de la carreta
        query = '''SELECT ca.id AS reel_store, c.id AS reel_id
        FROM cable_reel_assignment AS ca
        INNER JOIN cable_reel AS c ON c.id = ca.reel_id
        WHERE ca.user_id = %s AND c.serials = %s;
        '''
        values =[user_id, reel]
        c.execute(query, values)
        data = c.fetchone()
        #preguntamos si la carreta esta en el almacen
        if data is None:
            flash('La carreta no se encuantra en almacen')
        else:
            #eliminamos el registro de la carreta del almacen
            reel_id.append(data['reel_id'])
            query = 'UPDATE cable_reel_assignment SET register_active = false WHERE id = %s;'
            values = [data['reel_store']]
            c.execute(query, values)
            db.commit()
            flash('Carreta se retiro de almacen')
            
    return reel_id