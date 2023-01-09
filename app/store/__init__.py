from flask import Blueprint

store = Blueprint('store', __name__, url_prefix ='/store')

from . import routes
from . import tigo_store
from . import store_tech