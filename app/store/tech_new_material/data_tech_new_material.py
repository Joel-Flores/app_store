from flask import request,session, g

from .assign_teams import assign_teams
from .assign_materials import assign_materials
from .assign_reels import assign_reels
def data_tech_new_material():
    #actualizamos y registramos los materiales de tecnico y del almacen
    assign_materials()
    #agrega los equipos al tecnico o manda un mensaje de el equipo no se encuantra en el almacen
    assign_teams(request.form['series'].split("\r\n"), session.get('technical_name'), g.user['id'])
    #agrega las carretas al tecnico y los desvincula del almacen
    assign_reels(request.form['reel'].split("\r\n"), session.get('technical_name'), g.user['id'])
    session['technical_name'] = None