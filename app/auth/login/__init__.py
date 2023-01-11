from flask import render_template, redirect, url_for, flash
from app.auth.login.init_session import init_session

def logic_login():
    position_id, message = init_session()
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