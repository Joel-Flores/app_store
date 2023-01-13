from app.store import store
from flask import session

@store.route('/details_equipment')
def details_equipment():
    return session.get('equipment_serials')

@store.route('/details_reel')
def details_reel():
    return session.get('reel_series')

@store.route('/details_client')
def details_client():
    return

@store.route('/details_invoice')
def details_invoice():
    return