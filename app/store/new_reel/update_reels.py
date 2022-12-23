from flask import flash

def update_reels(db, c, reels):
    reel_id = list()
    error = False
    for reel in reels:
        #traemos datos del sistema para no repetir series
        query = '''SELECT *
        FROM cable_reel
        WHERE serials = %s;
        '''
        values = [reel]
        c.execute(query, values)
        #controlamos si la serie ya esta registrada
        if c.fetchone() is not None:
            flash(f'la carreta con la serie: {reel}, ya esta registrado')
            error = True
        else:
            #ingresar carretas al sistema
            query = 'INSERT INTO cable_reel (serials, status_id) VALUES (%s, %s);'
            values = [reel, 1]
            c.execute(query, values)
            db.commit()
            
            #traer el id de la serie subida y guardarlo en una lista
            
            query = '''SELECT id
            FROM cable_reel
            WHERE serials = %s order by id DESC LIMIT 1;
            '''
            values = [reel]
            c.execute(query, values)
            reel_id.append(c.fetchone())
    return reel_id, error