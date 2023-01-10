def tech_reel(c, tech_id):
    query = '''SELECT c.id, c.serial
    FROM reel_assignment AS ca
    INNER JOIN cable_reel AS c ON c.id = ca.reel_id
    WHERE ca.user_id = %s AND ca.register_active = True AND ca.status_id = 3;
    '''
    values = [tech_id]
    c.execute(query, values)
    return c.fetchall()