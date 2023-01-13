def data_count_reel(c, user_id):
    query = '''SELECT count(*) AS count
    FROM reel_assignment AS cs
    INNER JOIN cable_reel AS c ON cs.reel_id = c.id
    WHERE cs.user_id = %s AND cs.register_active = TRUE;
    '''
    values = [user_id]
    c.execute(query, values)
    return c.fetchone()

def data_series_reel(c, user_id):
    query = '''SELECT cs.id, c.serial 
    FROM reel_assignment AS cs
    INNER JOIN cable_reel AS c ON cs.reel_id = c.id
    WHERE cs.user_id = %s AND cs.register_active = TRUE;
    '''
    values = [user_id]
    c.execute(query, values)
    return c.fetchall()