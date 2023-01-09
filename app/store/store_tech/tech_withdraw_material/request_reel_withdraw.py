from flask import request
def request_reel_withdraw(reels):
    request_id_withdraw = list()
    for reel in reels:
        bool_value = request.form.get(reel['serial'], False)
        print(bool_value)
        request_id_withdraw.append({'id': reel["id"],'bool': bool_value})
        
    return request_id_withdraw