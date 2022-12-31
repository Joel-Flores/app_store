from flask import request

from .update_for_cm_mac import update_for_cm_mac
from .update_for_serials import update_for_serials
'cambie los cm_two y cars para usar la funcion de register y borrar los socumentos repetidos'
from app.store.warehouse_function import register
def update_equipment(db, c, user_id):
    cm_macs = request.form['cm_mac'].split("\r\n")
    cm_twos = request.form['cm_two'].split("\r\n")
    cards = request.form['card'].split("\r\n")
    model_id = request.form['name_equipment']
    
    if cm_twos == [""] and  cards == [""]:
        cm_twos = list()
        cards = list()
        for cm_mac in cm_macs:
            cm_twos.append(0)
            cards.append(0)
    
    serials_id, error = update_for_serials(db, c, cm_macs, cm_twos, cards, model_id, user_id)
    
    #retornamos los id de las series nuevas registradas
    return serials_id, error