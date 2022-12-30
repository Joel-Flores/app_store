from flask import request
def request_equipment_withdraw(equipments):
    request_id_withdraw = list()
    for equipment in equipments:
        try:
            id = request.form[equipment['cm_mac']]
            request_id_withdraw.append({'id': equipment["id"],'bool': True})
        except:
            request_id_withdraw.append(({'id': equipment["id"],'bool': True}))
        
    return request_id_withdraw