from flask import render_template, request, g
from .data_post import equipment_detail
from app.store.supplier_store.route_new_serial.data_get import model_equipment

def post_details_equipment():
    
    id_model = int(request.form['name_equipment'])
    id_status = int(request.form['option_filter'])
    
    response = equipment_detail(g.user['id'], id_model, id_status)
    models = model_equipment()
    return render_template('/store/details_store/details_equipment_filter.html', equipments = models, equipment_filter = response)

def get_details_equipment():
    models = model_equipment()
    return render_template('/store/details_store/details_equipment_all.html', equipments = models)