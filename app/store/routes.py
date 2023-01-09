#importar la configurcion del blueprint
from . import store

#funcion para la ruta de index
from .index import logic_index

"""
pagina pricipal del almacen"""
@store.route('/')
def index():
    return logic_index()
