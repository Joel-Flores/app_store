from flask import request, g, flash
from app.db import get_db

from .update_reels import update_reels
from .update_reel_store import update_reel_store

def data_new_reel():
    db, c = get_db()
    
    reels = request.form['reels'].split("\r\n")
    user_id = g.user['id']
    #ingresar las carretas al sistema y traer un lista con los id de las carretas 
    reel_id, error = update_reels(db, c, reels)
    #agregar las carretas al almacen
    if error is False:
        #asignando los carretas al almacen
        update_reel_store(db, c, reel_id, user_id)
        flash('Carretas Subidas')
    else:
        flash('error al ingresar las series')