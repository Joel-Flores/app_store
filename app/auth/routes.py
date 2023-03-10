#importar la del bp de auth
from . import auth

#importacion de frameworks
from flask import render_template, redirect, url_for, request, session, flash, g
import functools

#importacion de la conexion a la base de datos
from app.db import get_db

from .new_user import new_user
from .login import logic_login

#regitrar a un nuevo usuario
@auth.route('/register', methods = ['GET','POST'])
def register():
    #verificamos que el metodo sea post
    if request.method == 'POST':
        #mandamos a la funcion de registrar usuarios y redireccionamos a login
        flash(new_user())
        return redirect(url_for('auth.login'))
    #si el metodo es get mandamos el formulario de registro
    return render_template('auth/register.html')
    
#iniciar sesion del usuaio
@auth.route('/login', methods = ['GET','POST'])
def login():
    #verificamos el metodo post
    if request.method == 'POST':
        #mandamos la logica a la funcion que se ocupa de la logica
        return logic_login()
    return render_template('auth/login.html')

#cerrar session del usuario
@auth.route('/logout')
def logout():
    #borramos todos los datos y devolvemos al login
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