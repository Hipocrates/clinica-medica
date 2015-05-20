# -*- coding: utf-8 -*-
from openerp.osv import osv, fields

class diagnostico_detalle(osv.osv):
    
    _name = "diagnostico.detalle"
    _columns = {
        "id_dx_detalle" : fields.integer("Clave diagnostico detalle"),
        "id_diagnostico" : fields.many2one("diagnostico", "Diagnostico"),
        "id_cat_diagnostico" : fields.many2one("cat.diagnostico", "Catalogo diagnostico"),
        "prioridad" : fields.char("Prioridad"),
                
    }
diagnostico_detalle()
