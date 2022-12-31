from flask import request, session
from werkzeug.security import check_password_hash

from app.db import get_db


def init_session():
    db, c = get_db()
        
    username = request.form['username']
    password = request.form['password']
    error = None
    
    #bucamos si el usuario esta registrado
    query = '''SELECT u.id, u.password, u.register_active, s.user_name, s.user_lastname, p.id AS position
	FROM user AS u
	INNER JOIN staff AS s
    ON u.staff_id = s.id
    INNER JOIN positions AS p
    ON s.positions_id = p.id
    WHERE u.username = %s'''
    c.execute(query,[username])
    user = c.fetchone()
    
    #hacemos las verificaciones basicas
    if user is None:
        error = 'Usuario y/o Contraseña invalida'
    elif not check_password_hash(user['password'],password):
        error = 'Usuario y/o Contraseña invalida' 
    elif user['register_active'] is False:
        error = 'Permiso Denegado'
    
    #verificamos si hay las verificaciones fallaron
    if error is None:
        """
        borramos la session 
        creamos una session nueva con el id del usuario para posteriores consultas
        y mandamos mensaje de bienvanida al usuario.
        """
        
        session.clear()
        session['user'] = user
        error = f'{user["user_name"]} {user["user_lastname"]}, Bienvenido!'
        return user['position'], error
    
    #mandamos error en caso de que falle las verificaciones
    return False, error