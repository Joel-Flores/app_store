from flask import request, session, g, flash
from app.db import get_db
from app.for_request_material import request_material
from app.warehouse_function import register, update, delete, insert

def request_reel_withdraw(reels):
    request_id_withdraw = list()
    for reel in reels:
        bool_value = True
        
        if request.form.getlist(reel['serial']) == []:
            bool_value = False
        request_id_withdraw.append({'id': reel["id"],'bool': bool_value})
        
    return request_id_withdraw

def reel(user_id, tech, tech_reel):
    db, c = get_db()
    #mandamos los equipos del tecnico, cuales equipos devolivio
    options = request_reel_withdraw(tech_reel)
    for option in options:
        #preguntamos que equipos devolvieron
        if option['bool'] is not False:
            #eliminamos la carreta del registro del almacen
            delete.cable_reel(db, c, option['id'])
            #agregamos al registro que devolio el equipo
            insert.reel(db, c, user_id, option['id'], tech['id'], 8)
            #eliminamos los registros de signacion al tecnico y del almacen 
            delete.reel(db, c, option['id'])
        
    flash('carretas devuletas a almacen')

def request_equipment(equipments):
    request_id_withdraw = list()
    for equipment in equipments:
        bool_value = True
        if request.form.getlist(equipment['cm_mac']) == []:
            bool_value = False
        request_id_withdraw.append({'id': equipment["id"],'bool': bool_value})
        
    return request_id_withdraw

def teams(user_id, tech, tech_equipment):
    db, c = get_db()
    #mandamos los equipos del tecnico, cuales equipos devolivio
    options = request_equipment(tech_equipment)
    for option in options:
        #preguntamos que equipos devolvieron
        if option['bool'] is not False:
            #eliminamos los registros de signacion al tecnico
            delete.equipments(db, c, option['id'])
            #agregamos al registro que devolio el equipo
            insert.equipment(db, c, user_id, option['id'], tech['id'], 4)
            
    flash('equipos devuletos a almacen')

def materials(user_id, material_user, tech, material_tech):
    db, c = get_db()
    #mandamos a traer los materiales a un paquete especifico para esta funcion
    material_dict, material_list = request_material()
    #registramos los materiales
    material = register.material(db, c, material_list, user_id)
    #descontamos los materiales del tecnico
    error = update.update_tech_store(db, c, material_dict, material_tech, False)
    if error is False:
        #actualizamos materiales del almacen
        error = update.update_tech_store(db, c, material_dict, material_user, True)
        
        if error is False:
            insert.material(db, c, user_id, material['id'], tech['id'], 4)
            flash('materiales registrados')
            
        else:
            flash('no se registro al almacen, error las las cantidades digitadas')
            
    else:
       flash('no se registro al almacen, error las las cantidades digitadas')

def withdraw_material():
    user_id = g.user['id']
    user_material = session.get('materials')
    tech_name = session.get('technical_name')
    tech_material = session.get('technical_materials')
    tech_equiment = session.get('technical_equipments')
    tech_reel = session.get('technical_reels')
    
    materials(user_id, user_material, tech_name, tech_material)
    teams(user_id, tech_name, tech_equiment)
    reel(user_id, tech_name, tech_reel)