from flask import request
def request_equipment(equipments):
    request_id_withdraw = list()
    for equipment in equipments:
        bool_value = request.form.get(equipment['cm_mac'], False)
        request_id_withdraw.append({'id': equipment["id"],'bool': bool_value})
        
    return request_id_withdraw