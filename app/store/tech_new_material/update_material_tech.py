from flask import session, flash
def update_material_tech(db, c, added_material):
    #traemos todos las materiales y el id del tecnico
    tech = session.get('technical_name')
    tech_id = tech['id']
    query = '''SELECT m.id, m.cable_hdmi, m.cable_rca, m.spliter_two, m.spliter_three, m.remote_control,
    m.connector_int, m.connector_ext, m.power_supply, m.q_span, m.cp_black, m.sp_black, m.sp_withe, m.satellite_dish, m.lnb
    FROM material_assignment AS mt
    INNER JOIN materials AS m ON m.id = mt.material_id
    WHERE mt.user_id = %s AND mt.register_active = true;
    '''
    values = [tech_id]
    c.execute(query, values)
    material_tech = c.fetchone()
    
    #sumamos los materiales del tecnico con los asignados del almacen
    values = list()
    for key in added_material:
        values.append(material_tech[key] + added_material[key])
    
    values.append(material_tech['id'])
    #actualizamos los materiales del tecnico
    query = '''UPDATE materials
    SET cable_hdmi = %s,
    cable_rca = %s,
    spliter_two = %s,
    spliter_three = %s,
    remote_control = %s,
    connector_int = %s,
    connector_ext = %s,
    power_supply = %s,
    q_span = %s,
    cp_black = %s,
    sp_black = %s,
    sp_withe = %s,
    satellite_dish = %s,
    lnb = %s
    WHERE id = %s;'''
    c.execute(query, values)
    db.commit()
    flash('Materiales asignados actualizado')