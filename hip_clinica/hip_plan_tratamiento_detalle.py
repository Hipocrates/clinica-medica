# -*- coding: utf-8 -*-
from openerp.osv import osv, fields

class plan_tratamiento_detalle(osv.osv):
    
    _name = "plan.tratamiento.detalle"
    _columns = {
        #"id_plan_tx_detalle" : fields.integer("id plan tx detalle"),
        #"id_plan_tx" : fields.integer("id plan tx"),
        "id_cat_tratamiento" : fields.many2one("cat.tratamiento", "Catalogo de tratamiento"),
        "orden" : fields.char("Orden"),
        "fecha" : fields.date("Fecha"),
        "precio" : fields.float("precio", digits=(12,2)),
#         "tratamiento_id" : fields.many2one("plan.tratamiento", "Tratamiento"),
        "diagnostico_id" : fields.many2one("diagnostico", "Diagnostico"),
#         "factura_id" : fields.many2one("account.invoice", "Factura"),
        "paciente_id" : fields.many2one("res.partner", "Paciente"),  
        "state" : fields.selection([("draft", "Nuevo"), 
                                    ("done", "Revisado")], "Status"),          
    }
    
    def signal_done(self, cr, uid, ids, context=None):        
        self.write(cr, uid, ids, {"state" : "done"})        
        return True
    
    def create(self, cr, uid, vals, context=None):
        
        if vals.has_key("diagnostico_id"):
            d_id = vals["diagnostico_id"]
            diagnostico = self.pool.get("diagnostico").browse(cr, uid, d_id)
            
            if diagnostico.paciente_id:
                p_id = diagnostico.paciente_id.id
                vals["paciente_id"] = p_id 
        
        return super(plan_tratamiento_detalle, self).create(cr, uid, vals, context)        
#             if diagnostico.fecha:                
#                 vals["fecha"] = diagnostico.fecha
    
    _defaults = {
        "state" : "draft"
    }
plan_tratamiento_detalle()
