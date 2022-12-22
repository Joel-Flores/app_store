from flask import g, session, flash

def register_material_tech(db, c, values):
    #agregar el registro de los materiales asignados al tecnico
    query = '''INSERT INTO materials
    (cable_hdmi, cable_rca, spliter_two, spliter_three, remote_control,
    connector_int, connector_ext, power_supply, q_span,
    cp_black, sp_black, sp_withe, satellite_dish,
    lnb, status_id, created_by)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
    values.append(2)
    values.append(g.user['id'])
    c.execute(query, values)
    db.commit()
    
    #extraemos en id de los materiales que registramos del tecnico
    query = 'SELECT id FROM  materials WHERE created_by = %s ORDER BY id DESC LIMIT 1;'
    values = [g.user['id']]
    c.execute(query, values)
    material_id = c.fetchone()
    tech_id = session.get('technical_name')
    tech_id = tech_id['id']
    
    #ponemos el registro en la tabla de asignaciones desactivado para junto al id del tecnico, para un registro historico
    query = 'INSERT INTO material_assignment(user_id, material_id, register_active) VALUES(%s, %s, %s)'
    values = [tech_id, material_id['id'], False]
    c.execute(query, values)
    db.commit()
    flash('materiales registrados')