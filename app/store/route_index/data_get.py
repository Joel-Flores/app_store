from app.db import get_db

def data_technical():
    db, c = get_db()
    query = '''SELECT u.id, s.user_name, s.user_lastname
    FROM user AS u
    INNER JOIN staff AS s ON u.staff_id = s.id
    WHERE  s.positions_id = 3 AND u.register_active = TRUE
    GROUP BY u.id, s.user_name, s.user_lastname;'''
    c.execute(query)
    return c.fetchall()