# -*- coding: utf-8 -*-
from openerp.osv import osv, fields
from hip_clinica.receta import receta

class maestro(osv.osv):
    
    _name = "maestro"
    _columns = {
        "id_maestro" : fields.integer("id maestro"),
        "nombre" : fields.char("Nombre"),
        "cedula" : fields.char("Cedula"),
    }
maestro()