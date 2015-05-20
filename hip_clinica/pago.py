# -*- coding: utf-8 -*-
from openerp.osv import osv, fields
from hip_clinica.receta import receta

class pago(osv.osv):
    
    _name = "pago"
    _columns = {
        #"id_pago" : fields.integer("id pago"),
        #"id_consulta" : fields.integer("id consulta"),
        "precio" : fields.char("Precio"),
    }
pago()