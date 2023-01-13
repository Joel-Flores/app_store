from flask import request
def request_reel_withdraw(reels):
    request_id_withdraw = list()
    for reel in reels:
        bool_value = True
        if request.form.getlist(reel['serial']) == []:
            bool_value = False
        request_id_withdraw.append({'id': reel["id"],'bool': bool_value})
        
    return request_id_withdraw