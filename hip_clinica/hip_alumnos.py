# -*- coding: utf-8 -*-
from openerp.osv import osv, fields

class alumnos(osv.osv):
    
    _name = "alumnos"
    _columns = {
        #"id_receta" : fields.integer("id receta"),
        #"id_consulta" : fields.integer("id consulta"),
        "matricula" : fields.char("Matricula"),
        "nombre" : fields.char("Nombre"),
        "grupo" : fields.char("Grupo"),
        "ciclo" : fields.char("Ciclo"),
        #"id_carrera" : fields.char("id carrera"),
        "id_alumno" : fields.integer("Clave alumno"),
        "especialidad" : fields.selection([("odontologia", "Odontologia"),
                                           ("espendodoncia", "Esp. en Endodoncia"),
                                           ("esportodoncia", "Esp. en Ortodoncia"),
                                           ("esprehabilitacion", "Esp. en Rehabilitacion e Implantacion Oral")], "Especialidad")
                
    }
alumnos()