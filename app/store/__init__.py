from flask import Blueprint

store = Blueprint('store', __name__, url_prefix ='/store')

from . import routes
from . import supplier_store
from . import store_tech
from . import store_supplier
from . import equipment_invoice_client
from . import details_store