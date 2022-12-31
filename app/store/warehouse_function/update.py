def update_tech_store(db, c, new_material, material_user, funcion):
    values = list()
    error = False
    if funcion is True:
        for key in new_material:
            values.append(material_user[key] + new_material[key])
    else:
        for key in new_material:
            if material_user[key] >= 0 and material_user[key] - new_material[key] >= 0:
                values.append(material_user[key] - material_user[key])
            else:
                error = True
                return error
    query = '''UPDATE materials SET cable_hdmi = %s, cable_rca = %s, spliter_two = %s, 
    spliter_three = %s, remote_control = %s, connector_int = %s, connector_ext = %s, power_supply = %s, 
    q_span = %s, cp_black = %s, sp_black = %s, sp_withe = %s, satellite_dish = %s, lnb = %s WHERE id = %s;'''
    values.append(material_user['id'])
    c.execute(query, values)
    db.commit()