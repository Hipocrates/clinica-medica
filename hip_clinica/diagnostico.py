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
        "estatus" : fields.selection([("open", "Abierto"), 
                                      ("close", "Cerrado")], "Estatus")
                
    }
    
diagnostico()
