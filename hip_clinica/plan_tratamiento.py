# -*- coding: utf-8 -*-
from openerp.osv import osv, fields

class plan_tratamiento(osv.osv):
    
    _name = "plan.tratamiento"
    _columns = {
        "id_plan_tx" : fields.integer("Clave"),
        "fecha" :  fields.date("Fecha"),
        "estatus" : fields.selection([("open", "Abierto"), 
                                      ("close", "Cerrado")], "Estatus"),
        "id_diagnostico" : fields.many2one("diagnostico", "Diagnostico"),       
                
    }
    
plan_tratamiento()
