from flask import flash

def update_material(db, c, added_material, material_user):
    
    #sumamos los materiales del usuario con los asignados del almacen
    values = list()
    for key in added_material:
        values.append(material_user[key] + added_material[key])
    
    values.append(material_user['id'])
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