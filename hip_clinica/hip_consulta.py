# -*- coding: utf-8 -*-
from openerp.osv import osv, fields

class hip_consulta(osv.osv):
    
    _name = "hip.consulta"
    
    _columns = {
        "name" : fields.char("Folio"),
        "partner_id" : fields.many2one("res.partner", "Paciente"),
        "fecha" : fields.date("Fecha"),
        "maestro_id" : fields.many2one("maestro", "Maestro"),
        "alumno_id" : fields.many2one("alumnos", "Alumno"),
        "diagnostico_lines" : fields.one2many("diagnostico", "consulta_id", "Diagnostico"),
        "state" : fields.selection([("draft", "Borrador"),
                                    ("done", "Realizada")], "Estatus") 
    }
    
    _defaults = {
        "state" : "draft"
    }
    
hip_consulta()