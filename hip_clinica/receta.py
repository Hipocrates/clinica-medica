# -*- coding: utf-8 -*-
from openerp.osv import osv, fields

class receta(osv.osv):
    
    _name = "receta"
    _columns = {
        #"id_receta" : fields.integer("id receta"),
        #"id_consulta" : fields.integer("id consulta"),
        "fecha" : fields.date("Fecha"),
                
    }
receta()
