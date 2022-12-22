from flask import request, flash

def update_equipment(db, c, user_id):
    serials = request.form['series'].split("\r\n")
    model_id = request.form['name_equipment']
    error = False
    
    serials_id = list()
    for serial in serials:
        
        query = 'SELECT * FROM serial_equipments WHERE cm_mac = %s;'
        values = [serial]
        c.execute(query, values)
        if c.fetchone() is not None:
            flash(f'La serie {serial} esta registrado en el sistema')
            error = True
        else:
            #ingresar las series al sistema
            query = '''INSERT INTO serial_equipments (cm_mac, model_id, status_id, created_by)
            VALUES (%s, %s, %s, %s);'''
            values = [serial, model_id, 1, user_id]
            c.execute(query, values)
            db.commit()
            
            #traer el id de la serie subida y guardarlo en una lista
            query = '''SELECT id
            FROM serial_equipments
            WHERE created_by = %s order by id DESC LIMIT 1;
            '''
            values = [user_id]
            c.execute(query, values)
            serials_id.append(c.fetchone())
    #retornamos los id de las series nuevas registradas
    return serials_id, error