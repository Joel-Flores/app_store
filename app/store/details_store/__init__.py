from app.store import store
from flask import request, flash

from .route_details_equipment import post_details_equipment, get_details_equipment
from .route_details_invoice import post_details_invoice, get_details_invoice
def message_in_flash(messages):
    for message in messages:
        flash(message)

@store.route('/details_equipment', methods = ['GET','POST'])
def details_equipment():
    if request.method == 'POST':      
        return post_details_equipment()
    
    return get_details_equipment()

@store.route('/details_invoice', methods = ['GET','POST'])
def details_invoice():
    if request.method == 'POST':
        return post_details_invoice()
    
    return get_details_invoice()