# -*- coding: utf-8 -*-
from openerp.osv import osv, fields

class diagnostico(osv.osv):
    
    _name = "diagnostico"
    _columns = {
        "name" : fields.char("Clave"),
        "paciente_id" : fields.many2one("res.partner", "Paciente"),
        "fecha" :  fields.date("Fecha"),
        "alumno_id" : fields.many2one("alumnos", "Alumnos"),
        "maestro_id" : fields.many2one("maestro", "Maestro"),
        "state" : fields.selection([("draft", "Abierto"), 
                                      ("done", "Cerrado")], "Estatus"),
#         "diagnostico_ids" : fields.one2many("diagnostico.detalle", "id_diagnostico", "Diagnostico a detalle"),
        "diagnostico_factura" : fields.many2one("account.invoice", "Factura"),
        "consulta_id" : fields.many2one("hip.consulta", "Consulta"),
        "catalogo_dx" : fields.many2one("cat.diagnostico", "Catalogo Diagnosticos"),
        "tratamiento_ids" : fields.one2many("plan.tratamiento.detalle", "diagnostico_id", "Tratamientos") 
                
    }
    
    _defaults = {
        "estatus" : "draft"
    }
    
    def signal_done(self, cr, uid, ids, context=None):        
        self.write(cr, uid, ids, {"estatus" : "close"})        
        return True
    
    def onchange_diagnostico(self, cr, uid, ids, d_id, context=None):
        
        r = {"value" : {}}
        
        if d_id:
            d_obj = self.pool.get("cat.diagnostico")
            d = d_obj.browse(cr, uid, d_id)
            r["value"].update({"name" : d.name})
        
        return r
    
diagnostico()
