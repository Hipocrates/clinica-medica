# -*- coding: utf-8 -*-
from openerp.osv import osv, fields

class diagnostico(osv.osv):
    
    _name = "diagnostico"
    _columns = {
        "name" : fields.char("Clave"),
        "paciente_id" : fields.many2one("res.partner", "Paciente", domain=[("tipo_persona", "=", "paciente")]),
        "fecha" :  fields.date("Fecha"),
        "alumno_id" : fields.many2one("res.partner", "Paciente", domain=[("tipo_persona", "=", "alumno")]),
        "maestro_id" : fields.many2one("res.partner", "Paciente", domain=[("tipo_persona", "=", "maestro")]),
        "estatus" : fields.selection([("open", "Abierto"), 
                                      ("close", "Cerrado")], "Estatus")
                
    }
    
diagnostico()
