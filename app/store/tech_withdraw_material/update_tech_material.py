from flask import session, flash
def update_tech_material(db, c, added_material):
    materials_tech = session.get('technical_materials')
    error = False
    values = list()
    #retiramos los materiales debueltos del tecnico
    for key in added_material:
        if materials_tech[key] >= 0 and materials_tech[key] - added_material[key] >= 0:
            values.append(materials_tech[key] - added_material[key])
        else:
            error = True
            flash('Error al descontar los materiales')
            return error
        
    values.append(materials_tech['id'])
    
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
    flash('Materiales del Tecnico actualizado')
    return error