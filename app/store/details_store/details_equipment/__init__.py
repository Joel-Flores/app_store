from flask import request, g
from app.db import get_db
from .equipment_detail import _equipment_detail
def logic_details_equipment():
    db, c = get_db()
    id_model = int(request.form['name_equipment'])
    id_status = int(request.form['option_filter'])
    message, values = _equipment_detail(c, g.user['id'], id_model, id_status)
    return message, values