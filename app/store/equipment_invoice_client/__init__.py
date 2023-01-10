#importar la configurcion del blueprint
from app.store import store
from flask import request, render_template, flash

from .equipment_client import logic_client
from .equipment_invoice import logic_invoice

def message_in_flash(messages):
    for message in messages:
        flash(message)
#poner el equipo en la lista de con cliente
@store.route('/equipment_client', methods = ['GET','POST'])
def equipment_client():
    if request.method == 'POST':
        response, message = logic_client()
        message_in_flash(message)
        return response
    return render_template('/store/equipment_invoice_client/form_equipment_client.html')

#facturar el equipo al tecnico
@store.route('/invoice_tech', methods = ['GET','POST'])
def invoice_tech():
    if request.method == 'POST':
        response, message = logic_invoice()
        message_in_flash(message)
        return response
    return render_template('/store/equipment_invoice_client/form_equipment_invoice.html')