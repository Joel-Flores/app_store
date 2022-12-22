from app.db import get_db

def data_form_new_equipment():
    db, c = get_db()
    c.execute('SELECT id, name_model FROM model_equipments WHERE id !=1;')
    return c.fetchall()