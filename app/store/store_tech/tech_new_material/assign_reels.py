from app.db import get_db

from app.warehouse_function import delete, insert, search

def assign_reels(reels, tech, user_id):
    message = list()
    db, c = get_db()
    error = False
    for reel in reels:
        #buscar id de la carreta
        reel_id = search.id_reel(c, reel)
        if reel_id is None:
            message.append('carreta no registrada')
            error = True
        else:
            #retirar las carretas del resgistro del almacen
            delete.reel(db, c, reel_id['id'])
            #asignar carreta al registro del tecnico
            insert.reel(db, c, tech['id'], reel_id['id'], user_id, 3)
    if error is False:
        message.append('carretas asignados al tecnico')
    return message