def data_count_reel(c, user_id):
    query = '''SELECT count(*) AS count
    FROM cable_reel_store AS cs
    INNER JOIN cable_reel AS c ON cs.reel_id = c.id
    WHERE cs.user_id = %s AND cs.register_active = TRUE AND cs.status_id = 1;
    '''
    values = [user_id]
    c.execute(query, values)
    return c.fetchone()

def data_series_reel(c, user_id):
    query = '''SELECT cs.id, c.serial 
    FROM cable_reel_store AS cs
    INNER JOIN cable_reel AS c ON cs.reel_id = c.id
    WHERE cs.user_id = %s AND cs.register_active = TRUE AND cs.status_id = 1;
    '''
    values = [user_id]
    c.execute(query, values)
    return c.fetchall()