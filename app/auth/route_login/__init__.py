from flask import render_template, redirect, url_for, flash
from .data_post import post

def post_login():
    position_id, message = post()
    if position_id is False:
        flash(message)
        return render_template('auth/login.html')
    
    flash(message)
    if position_id == 3:
        return redirect(url_for('tech.index'))
    
    elif position_id == 2:
        return redirect(url_for('store.index'))
    
    else:
        return redirect(url_for('admin.index'))

def get_login():
    return render_template('auth/login.html')