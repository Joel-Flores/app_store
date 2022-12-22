from flask import g, flash
def update_store_material(db, c, added_material):
    materials_store = g.materials
    error = False
    values = list()
    #descontamos los materiales de almacen asignados al tecnico
    for key in added_material:
        if materials_store[key] >= 0 and materials_store[key] - added_material[key] >= 0:
            values.append(materials_store[key] - added_material[key])
        else:
            error = True
            flash('No tienes los materiales suficientes en almacen')
            flash('no se asigno los materiales correctamente')
            return error
        
    values.append(materials_store['id'])
    
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
    flash('Materiales del Almacen actualizado')
    return error