from flask import g, flash

def update_material_store(db, c, added_material):
    #traemos todos las materiales y el id asignados al tecnico
    material_store = g.materials
    
    #sumamos los materiales del tecnico con los asignados del almacen
    values = list()
    for key in added_material:
        values.append(material_store[key] + added_material[key])
    
    values.append(material_store['id'])
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