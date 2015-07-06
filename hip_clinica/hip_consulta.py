# -*- coding: utf-8 -*-
from openerp.osv import osv, fields

class hip_consulta(osv.osv):
    
    _name = "hip.consulta"
    
    def signal_done(self, cr, uid, ids, context=None):        
        self.write(cr, uid, ids, {"state" : "done"})        
        return True
    
    def create(self, cr, uid, vals, context=None):
        vals['name'] = self.pool.get('ir.sequence').get(cr, uid, 'hip.consulta') or '/'
        return super(hip_consulta, self).create(cr, uid, vals, context=context)
    
    def get_company(self, cr, uid, context=None):
        obj = self.pool.get("res.users")
        user = obj.browse(cr, 1, [uid])
        return user.company_id.id
    
    def onchange_partner(self, cr, uid, ids, partner_id, context=None):
        r = {"value" : {}}
        
        partner = self.pool.get("res.partner")
        
        if partner.edad:
            r["value"].update({"edad" : partner.edad})
        
        if partner.genero:
            r["value"].update({"genero" : partner.genero})
        
        return r
    
    _columns = {
        "name" : fields.char("Folio", readonly=True, store=True),
        "edad" : fields.integer("Edad"),
        "genero" : fields.selection([("masculino", "Masculino"), 
                                     ("femenino", "Femenino")], "Genero"),
        "partner_id" : fields.many2one("res.partner", "Paciente"),
        "fecha" : fields.date("Fecha"),
        "maestro_id" : fields.many2one("maestro", "Maestro"),
        "alumno_id" : fields.many2one("alumnos", "Alumno"),
        "diagnostico_lines" : fields.one2many("diagnostico", "consulta_id", "Diagnostico"),
        "state" : fields.selection([("draft", "Borrador"),
                                    ("done", "Realizada")], "Estatus"),
        "company_id" : fields.many2one("res.company", "Company"),
    }
    
    _defaults = {
        "state" : "draft",
        "company_id" : get_company
    }
    
hip_consulta()