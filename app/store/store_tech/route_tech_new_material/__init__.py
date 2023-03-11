from flask import render_template, redirect, url_for, request, session, g
from app.auth.user_data import data_user
from .data_post import assingn
def post_tech_new_material():
    assingn()
    data_user()
    return redirect(url_for('store.index'))

def get_tech_new_material():
    return render_template('/store/store_tech/tech_new_material_form.html')