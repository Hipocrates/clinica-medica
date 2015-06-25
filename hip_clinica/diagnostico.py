# -*- coding: utf-8 -*-
from openerp.osv import osv, fields

class diagnostico(osv.osv):
    
    _name = "diagnostico"
    
#     def _get_paciente(self, cr, uid, ids, field_name, args, context=None):
#         
#         r = {}        
        
#         obj = self.browse(cr, uid, ids, context)
#         
#         if obj.consulta_id:
#             c_id = obj.consulta_id[0].id
#             consulta = self.pool.get("hip.consulta").browse(cr, uid, c_id)
#             p_id = consulta.partner_id.id
#             
#             self.write(cr, uid, ids, {"paciente_id" : p_id})
#             
#             r[ids[0]] = p_id
            
#         return r
    
    def create(self, cr, uid, vals, context=None):
        
        if vals.has_key("consulta_id"):
            c_id = vals["consulta_id"]
            consulta = self.pool.get("hip.consulta").browse(cr, uid, c_id)
            
            if consulta.partner_id:
                p_id = consulta.partner_id.id
                vals["paciente_id"] = p_id 
                
            if consulta.fecha:                
                vals["fecha"] = consulta.fecha 
        
        return super(diagnostico, self).create(cr, uid, vals, context)
    
    def write(self, cr, uid, ids, vals, context=None):
        return super(diagnostico, self).write(cr, uid, ids, vals, context)
      
    _columns = {
        "name" : fields.char("Clave"),
#         "paciente_id" : fields.function(_get_paciente, type='many2one', string='Paciente'),
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
        "state" : "draft"
    }
    
    def signal_done(self, cr, uid, ids, context=None):        
        self.write(cr, uid, ids, {"state" : "done"})        
        return True
    
    def onchange_diagnostico(self, cr, uid, ids, d_id, context=None):
        
        r = {"value" : {}}
        
        if d_id:
            d_obj = self.pool.get("cat.diagnostico")
            d = d_obj.browse(cr, uid, d_id)
            r["value"].update({"name" : d.name})
        
        return r
    
diagnostico()
