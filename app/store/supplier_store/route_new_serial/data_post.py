from flask import g, request, flash
from app.db import get_db
from app.warehouse_function import register, insert, update

def _list_zero(equipments):
    cm_two = list()
    cards = list()
    
    for value in equipments:
        cm_two.append(0)
        cards.append(0)
        
    return cm_two, cards

def _request_form():
    cm_macs = request.form['cm_mac'].split("\r\n")
    cm_twos = request.form['cm_two'].split("\r\n")
    cards = request.form['card'].split("\r\n")
    model_id = request.form['name_equipment']
    
    if cm_twos == [""] and  cards == [""]:
        cm_twos, cards = _list_zero(cm_macs)
    
    return cm_macs, cm_twos, cards, model_id
    
def new_serial():
    db, c = get_db()
    user_id = g.user['id']
    cm_macs, cm_twos, cards, model_id = _request_form()
    error = None
    
    for cm_mac, cm_two, card in zip(cm_macs, cm_twos, cards):
        query = 'SELECT * FROM equipments_serial WHERE cm_mac = %s;'
        values = [cm_mac]
        print(cm_mac)
        c.execute(query, values)
        data = c.fetchone()
        
        if not data is None:
            update.equipment(db, c, data['id'])
            flash(f'El equipo: {cm_mac}, esta registrado en el sistema, veifica si los datos estan correctos en el buscador')
            error = True
            
        else:
            #ingresar las series al sistema
            values = [cm_mac, cm_two, card, model_id]
            serial = register.equipment(db, c, values, user_id)
            insert.equipment(db, c, user_id, serial['id'], user_id, 1)
   
    if error is None:
        flash('Equipos Subidos al Almacen')