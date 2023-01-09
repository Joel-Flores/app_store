from flask import flash 
from app.warehouse_function import register, insert, update
def update_for_serials(db, c, cm_macs, cm_twos, cards, model_id, user_id):
    error = False
    for cm_mac, cm_two, card in zip(cm_macs, cm_twos, cards):
        
        query = 'SELECT * FROM equipments_serial WHERE cm_mac = %s;'
        values = [cm_mac]
        c.execute(query, values)
        data = c.fetchone()
        if data is not None:
            update.equipment(db, c, data['id'])
            flash(f'El equipo: {cm_mac}, esta registrado en el sistema')
            error = True
        else:
            #ingresar las series al sistema
            values = [cm_mac, cm_two, card, model_id]
            serial = register.equipment(db, c, values, user_id)
            insert.equipment(db, c, user_id, serial['id'], user_id, 1)
    return error