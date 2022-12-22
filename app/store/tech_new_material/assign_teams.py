#importamos las herramientas necesarias
from app.db import get_db
from flask import flash

def assign_teams(equipments, tech, user_id):
    db, c = get_db()
    error = True
    tech_id = tech['id']
    #query para extraer el id del equipo en el almacen y la serie
    for equipment in equipments:
        query = '''SELECT ea.id, ea.serial_id
        FROM equipment_assignment AS ea
        INNER JOIN serial_equipments AS se ON ea.serial_id = se.id
        WHERE cm_mac = %s AND ea.user_id = %s AND ea.register_active = TRUE;
        '''
        #agregamos los valores de la serie del equipo y el id del usuario de almacen
        values = [equipment, user_id]
        c.execute(query, values)
        serial_id = c.fetchone()
        #consultamos si hay registro en el almacen
        if serial_id is None:
            flash(f'equipo {equipment} no registrado en almacen')
        else:
            error = False
            #eliminamos el registro del almacen para asignarlo al tecnico
            query = 'UPDATE equipment_assignment SET register_active = FALSE WHERE id = %s;'
            values = [serial_id['id']]
            c.execute(query, values)
            #agregamos la serie al tecnico
            query = 'INSERT INTO equipment_assignment(user_id, serial_id) VALUES(%s,%s)'
            values = [tech_id, serial_id['serial_id']]
            c.execute(query, values)
            db.commit()
    if error is False:
        flash('equipos asignados al tecnico') 