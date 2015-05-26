# -*- coding: utf-8 -*-
from openerp.osv import osv, fields

class plan_tratamiento(osv.osv):
    
    _name = "plan.tratamiento"
    _columns = {
#         "id_plan_tx" : fields.integer("Clave"),
        "name" : fields.integer("Clave"),
        "fecha" :  fields.date("Fecha"),
        "estatus" : fields.selection([("open", "Abierto"), 
                                      ("close", "Cerrado")], "Estatus"),
        "id_diagnostico" : fields.many2one("diagnostico", "Diagnostico"),  
        "tratamiento_ids" : fields.one2many("plan.tratamiento.detalle", "tratamiendo_id", "Tratamientos"),
        "id_alumno" : fields.many2one("alumnos","Alumno"),  
        "id_maestro" : fields.many2one("maestro","Maestro"),
        "id_paciente" : fields.many2one("res.partner","Paciente"),     
                
    }
    
plan_tratamiento()
