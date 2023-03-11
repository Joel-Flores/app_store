#importar la configurcion del blueprint
from app.store import store
from flask import request

from .route_equipment_client import post_equipment_client, get_equipment_client
from .route_tech_invoice import post_tech_invoice, get_tech_invoice

#poner el equipo en la lista de con cliente
@store.route('/equipment_client', methods = ['GET','POST'])
def equipment_client():
    if request.method == 'POST':
        return post_equipment_client()
    
    return get_equipment_client()

#facturar el equipo al tecnico
@store.route('/invoice_tech', methods = ['GET','POST'])
def invoice_tech():
    if request.method == 'POST':
        return post_tech_invoice()
    
    return get_tech_invoice()