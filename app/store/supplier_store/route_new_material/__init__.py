from flask import render_template, redirect, url_for
from .data_post import new_material
from app.auth.user_data import data_user

def post_new_material():
    new_material()
    data_user()
    return redirect(url_for('store.index'))

def get_new_material():
    return render_template('/store/tigo_store/form_new_material.html')