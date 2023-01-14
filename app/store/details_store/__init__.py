from app.store import store
from flask import request, render_template, flash

from app.store.tigo_store.new_serial import get_new_serial
from .details_equipment import logic_details_equipment

def message_in_flash(messages):
    for message in messages:
        flash(message)

@store.route('/details_equipment', methods = ['GET','POST'])
def details_equipment():
    if request.method == 'POST':
        message, response = logic_details_equipment()
        message_in_flash(message)
        return render_template('/store/details_store/details_equipment_filter.html', equipments = get_new_serial(), equipment_filter = response)
    return render_template('/store/details_store/details_equipment_all.html', equipments = get_new_serial())


@store.route('/details_client')
def details_client():
    return

@store.route('/details_invoice')
def details_invoice():
    return