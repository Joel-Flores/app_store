from app.db import get_db
def tech_reel(tech_id):
    db, c = get_db()
    query = '''SELECT c.id, c.serials
    FROM cable_reel_assignment AS ca
    INNER JOIN cable_reel AS c ON c.id = ca.reel_id
    WHERE ca.user_id = %s AND ca.register_active = True;
    '''
    values = [tech_id]
    c.execute(query, values)
    return c.fetchall()