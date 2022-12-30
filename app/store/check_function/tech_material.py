from app.db import get_db
def tech_material(tech_id):
    db, c = get_db()
    query = '''SELECT m.id, m.cable_hdmi, m.cable_rca, m.spliter_two, m.spliter_three, m.remote_control,
    m.connector_int, m.connector_ext, m.power_supply, m.q_span, m.cp_black, m.sp_black, m.sp_withe, m.satellite_dish, m.lnb
    FROM material_assignment AS mt
    INNER JOIN materials AS m ON m.id = mt.material_id
    WHERE mt.user_id = %s AND mt.register_active = true;
    '''
    values = [tech_id]
    c.execute(query, values)
    return c.fetchone()