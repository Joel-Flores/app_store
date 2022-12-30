from flask import flash

def register_material(db, c, values, status_id, store_id, tech_id):
    #agregar el registro de los materiales al sistema por el almacen
    query = '''INSERT INTO materials
    (cable_hdmi, cable_rca, spliter_two, spliter_three, remote_control,
    connector_int, connector_ext, power_supply, q_span,
    cp_black, sp_black, sp_withe, satellite_dish,
    lnb, status_id, created_by)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
    #en es status id va 1 para el almacen y 2 para el tecnico
    values.append(status_id)
    values.append(store_id)
    c.execute(query, values)
    db.commit()
    
    #extraemos en id de los materiales que registramos
    query = 'SELECT id FROM  materials WHERE created_by = %s ORDER BY id DESC LIMIT 1;'
    values = [store_id]
    c.execute(query, values)
    material_id = c.fetchone()
    
    ''' ponemos el registro en la tabla de
    asignaciones desactivado, para un registro historico '''
    query = 'INSERT INTO material_assignment(user_id, material_id, register_active) VALUES(%s, %s, %s)'
    #verificamos si tenemos tecnico para la asignacion
    if tech_id is not None:
        tech_id = tech_id['id']
        values = [tech_id, material_id['id'], False]
        c.execute(query, values)
        db.commit()
    else:
        values = [store_id, material_id['id'], False]
        c.execute(query, values)
        db.commit()
    flash('materiales registrados')