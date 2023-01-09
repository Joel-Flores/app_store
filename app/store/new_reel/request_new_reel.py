from flask import request, g, flash
from app.db import get_db

from .update_reels import update_reels

def request_new_reel():
    db, c = get_db()
    
    reels = request.form['reels'].split("\r\n")
    user_id = g.user['id']
    #ingresar las carretas al sistema y traer un lista con los id de las carretas 
    error = update_reels(db, c, reels, user_id)
    #mensaje exito al subir todas las carretas
    if error is False:
        flash('Carretas Subidas')