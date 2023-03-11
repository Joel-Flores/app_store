from flask import flash, redirect, url_for, render_template
from .data_post import post

def post_register():
    error = post()
    if error is None:
        flash('Registrado Exitosamente')
        return redirect(url_for('auth.login'))
    else:
        flash(error)
        return redirect(url_for('auth.register'))

def get_register():
    return render_template('auth/register.html')