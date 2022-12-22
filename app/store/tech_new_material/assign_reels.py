from app.db import get_db

from .update_store_reel import update_store_reel
from .update_tech_reel import update_tech_reel

def assign_reels(reels, tech, user_id):
    db, c = get_db()
    #retirar las carretas del resgistro del almacen
    reel_id = update_store_reel(db, c, reels, user_id)
    #asignar carretas al tecnico
    update_tech_reel(db, c, reel_id, tech['id'])
    return reel_id