from app.db import get_db

def model_equipment():
    db, c = get_db()
    sql = 'SELECT id, name_model FROM equipments_model WHERE id !=1;'
    c.execute(sql)
    return c.fetchall()