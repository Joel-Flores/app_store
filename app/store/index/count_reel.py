def count_reel(c, user_id):
    query = '''SELECT count(*) AS count
    FROM cable_reel_assignment AS ca
    INNER JOIN cable_reel AS c ON ca.reel_id = c.id
    WHERE ca.user_id = %s AND ca.register_active = TRUE;
    '''
    values = [user_id]
    c.execute(query, values)
    return c.fetchone()