# -*- coding: utf-8 -*-
from openerp.osv import osv, fields

class maestro(osv.osv):
    
    _name = "maestro"
    _columns = {
        "id_maestro" : fields.integer("id maestro"),
        "nombre" : fields.char("Nombre"),
        "cedula" : fields.char("Cedula"),
    }
maestro()