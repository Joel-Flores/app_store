from .update_store_reel import update_store_reel
from .update_tech_reel import update_tech_reel

def assign_reels(reels, tech, user_id):
    #retirar las carretas del resgistro del almacen
    reel_id = update_store_reel(reels, user_id)
    #asignar carretas al tecnico
    update_tech_reel(reel_id, tech['id'])
    pass