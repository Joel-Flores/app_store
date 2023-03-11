#importar la del bp de auth
from . import auth

from flask import redirect, url_for, request, session, flash, g
import functools

from .route_register import post_register, get_register
from .route_login import post_login, get_login

#regitrar a un nuevo usuario
@auth.route('/register', methods = ['GET','POST'])
def register():
    if request.method == 'POST':
        return post_register()

    return get_register()
    
#iniciar sesion del usuaio
@auth.route('/login', methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        return post_login()
    
    return get_login()

#cerrar session del usuario
@auth.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))

#protegemos rutas para que no ingresen sin haber iniciado session
@auth.before_app_request
def load_logged_in_user():
    user = session.get('user')
    
    if user is None:
        g.user= None
    else:
        g.user = user
    
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            flash('Inicia sesion')
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view