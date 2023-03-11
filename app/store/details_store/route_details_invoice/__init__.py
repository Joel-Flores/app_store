from flask import render_template
from .data_get import list_invoice_tech_all
from .data_post import list_equipment_invoice

def post_details_invoice():
    response = list_equipment_invoice()
    return render_template('/store/details_store/route_details_invoice/post_details_invoice.html', equipment_filter = response)

def get_details_invoice():
    response = list_invoice_tech_all()
    return render_template('/store/details_store/route_details_invoice/get_details_invoice.html', equipment_filter = response)