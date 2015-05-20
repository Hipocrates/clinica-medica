# -*- coding: utf-8 -*-
from openerp.osv import osv, fields

class plan_tratamiento_detalle(osv.osv):
    
    _name = "plan.tratamiento.detalle"
    _columns = {
        #"id_plan_tx_detalle" : fields.integer("id plan tx detalle"),
        #"id_plan_tx" : fields.integer("id plan tx"),
        "id_cat_tratamiento" : fields.many2one("cat.tratamiento", "Catalogo de tratamiento"),
        "orden" : fields.char("Orden"),
                
    }
plan_tratamiento_detalle()
