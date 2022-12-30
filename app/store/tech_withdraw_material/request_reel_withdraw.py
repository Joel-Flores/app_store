from flask import request
def request_reel_withdraw(reels):
    request_id_withdraw = list()
    for reel in reels:
        try:
            id = request.form[reel['serials']]
            request_id_withdraw.append({'id': reel["id"],'bool': True})
        except:
            request_id_withdraw.append(({'id': reel["id"],'bool': True}))
        
    return request_id_withdraw