from flask import g, session, request, flash
from app.db import get_db
from app.for_request_material import request_material
from app.warehouse_function import insert, register, update, search, delete

def reels(reels, tech, user_id):
    db, c = get_db()
    error = False
    for reel in reels:
        #buscar id de la carreta
        reel_id = search.id_reel(c, reel)
        if reel_id is None:
            flash('carreta no registrada')
            error = True
        else:
            #retirar las carretas del resgistro del almacen
            delete.reel(db, c, reel_id['id'])
            #asignar carreta al registro del tecnico
            insert.reel(db, c, tech['id'], reel_id['id'], user_id, 3)
    if error is False:
        flash('carretas asignados al tecnico')

def teams(equipments, tech, user_id):
    db, c = get_db()
    error = False
    for equipment in equipments:
        #buscar id de la serie
        equipment_id = search.id_equipment(c, equipment)
        #consultamos si hay registro en el almacen
        if equipment_id is None:
            flash(f'equipo {equipment} no registrado en almacen')
            error = True
        else:
            #eliminamos el registro del almacen
            delete.equipments(db, c, equipment_id['id'])
            #agregamos la serie al tecnico
            insert.equipment(db, c, tech['id'], equipment_id['id'], user_id, 3)
    if error is False:
        flash('equipos asignados al tecnico')

def materials(material_user, user_id, material_tech, tech):
    db, c = get_db()
    #mandamos a traer los materiales a un paquete especifico para esta funcion
    material_dict, material_list = request_material()
    #registramos los materiales
    material = register.material(db, c, material_list, user_id)
    #descontamos los materiales del almacen
    error = update.update_tech_store(db, c, material_dict, material_user, False)
    if error is False:
        #actualizamos materiales del technico
        error = update.update_tech_store(db, c, material_dict, material_tech, True)
        if error is False:
            insert.material(db, c, tech['id'], material['id'], user_id, 3)
            flash('materiales asignado correctamente')
        else:
            flash('no se registro al tecnico, error las las cantidades digitadas')
    else:
        flash('no se registro al almacen, error las las cantidades digitadas')
        
def assingn():
    user_id = g.user['id']
    name_tech = session.get('technical_name')
    material_tech = session.get('technical_materials')
    material_store = session.get('materials')
    series = request.form['series'].split("\r\n")
    reel = request.form['reels'].split("\r\n")
    
    #actualizamos y registramos los materiales de tecnico y del almacen
    materials(material_store, user_id, material_tech, name_tech)
    
    #agrega los equipos al tecnico o manda un mensaje de el equipo no se encuantra en el almacen
    teams(series, name_tech, user_id)
    
    #agrega las carretas al tecnico y los desvincula del almacen
    reels(reel, name_tech, user_id)