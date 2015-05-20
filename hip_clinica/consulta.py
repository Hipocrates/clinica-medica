# -*- coding: utf-8 -*-
from openerp.osv import osv, fields
from hip_clinica.receta import receta

class consulta(osv.osv):
    
    _name = "consulta"
#     _inherit = "account.invoice"
    _columns = {
        #"id_consulta" : fields.integer("id consulta"),
        "folio" : fields.char("Folio"),
        #"id_diagnostico" : fields.integer("id diagnostico"),
        "fecha" : fields.date("Fecha"),
        "id_paciente" : fields.many2one("res.partner")
        #"id_maestro" : fields.integer("id maestro"),
        #"id_paciente" : fields.integer("id paciente"),
        #"id_plan_tx" : fields.integer("id plan tx"),
        #"id_plan_tx_detalle" : fields.integer("id plan tx detalle"),
        
    }
consulta()