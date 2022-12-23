from flask import flash 

def update_for_serials(db, c, cm_macs, cm_twos, cards, model_id, user_id):
    error = False
    serials_id = list()
    for cm_mac, cm_two, card in zip(cm_macs, cm_twos, cards):
        
        query = 'SELECT * FROM serial_equipments WHERE cm_mac = %s;'
        values = [cm_mac]
        c.execute(query, values)
        if c.fetchone() is not None:
            flash(f'La serie: {cm_mac}, esta registrado en el sistema')
            error = True
        else:
            #ingresar las series al sistema
            query = '''INSERT INTO serial_equipments (cm_mac, cm_mac_two, card_number, model_id, status_id, created_by)
            VALUES (%s, %s, %s, %s, %s, %s);'''
            values = [cm_mac, cm_two, card, model_id, 1, user_id]
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
    return serials_id, error