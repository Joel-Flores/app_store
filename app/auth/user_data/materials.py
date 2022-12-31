def data_materials(c, user_id):
    query = '''SELECT m.id, m.cable_hdmi, m.cable_rca, m.spliter_two, 
    m.spliter_three, m.remote_control, m.connector_int, m.connector_ext,
    m.power_supply, m.q_span, m.cp_black, m.sp_black, m.sp_withe, m.satellite_dish, m.lnb
    FROM material_store_and_tech AS ma
    INNER JOIN materials AS m ON ma.material_id = m.id
    WHERE ma.user_id = %s AND ma.register_active = True;
    '''
    c.execute(query,[user_id])
    return c.fetchone()