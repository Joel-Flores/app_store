from flask import render_template, redirect, url_for
from .data_post import new_reel
from app.auth.user_data import data_user
def post_new_reel():
    new_reel()
    data_user()
    return redirect(url_for('store.index'))

def get_new_reel():
    return render_template('/store/tigo_store/form_new_reel.html')