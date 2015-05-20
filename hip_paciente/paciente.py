# -*- coding: utf-8 -*-
from openerp.osv import osv, fields

class partner_clinica(osv.osv):
    _inherit = "res.partner"
    
    _columns = {
        "tipo_persona" : fields.selection([("paciente", "Paciente"), 
                                           ("alumno", "Alumno"), 
                                           ("maestro", "Maestro")], "Tipo Persona"),
        "edad" : fields.integer("Edad"),
        "genero" : fields.selection([("masculino", "Masculino"), 
                                     ("femenino", "Femenino")], "Genero"),
        "lugar_de_nac" : fields.char("Lugar de Nacimiento"),
         "fecha_nac" : fields.date("Fecha de Nacimiento"),
         "ocupacion" : fields.char("Ocupacion"),
         "escolaridad" : fields.char("Escolaridad"),
         "estado_civil" : fields.selection([("soltero", "Soltero(a)"),
                                            ("casado", "Casado(a)"),
                                            ("viudo", "Viudo(a)"),
                                            ("divorciado", "Divorciado(a)" )], "Estado Civil"),
                "fecha_ultima_consulta" : fields.date("Fecha de ultima consulta"),
         "motivo_ultima_consulta" : fields.text("Motivo de ultima consulta"),
         
         
         "antecedentes_patologicos_hereditarios" : fields.text("Antecedentes Patologicos Hereditarios"),
         "antecedentes_personales_patologicos" : fields.text("Antecedentes personales patologicos"),
         "grupo_sanguineo" : fields.selection([("AB+", "AB+"),
                                               ("AB-", "AB-"),
                                               ("A+", "A+"),
                                               ("A-", "A-"),
                                               ("B+", "B+"),
                                               ("B-", "B-"),
                                               ("O+", "O+"),
                                               ("O-", "O-")], "Tipo de sangre"),
         "factor_rh" : fields.char("Factor Rh"),
         "cartilla_de_vacunacion" : fields.boolean("Cuenta con cartilla de vacunacion"),
         "esquema_completo" : fields.boolean("Esquema completo"),
         "dosis_faltante" : fields.boolean("Dosis faltante"),
         "adicciones" : fields.selection([("AB+", "AB+"),
                                               ("tabaco", "Tabaco"),
                                               ("alcohol", "Alcohol"),
                                               ("drogas", "Drogas")], "Adicciones"),
                "alergias" : fields.selection([("antiobioticos", "Antibioticos"),
                                               ("analgesicos", "Analgesicos"),
                                               ("alimentos", "Alimentos"),
                                               ("otro", "Otro")], "Alergico a: "),
         "especificaciones" : fields.char("Especificaciones"),
         "hospitalizado" : fields.boolean("Ha sido hospitalizado"),
         "fecha_ultima_hospitalizacion" : fields.date("Fecha de ultima hospitalizacion"),
         "motivo_ultima_hospitalizacion" : fields.char("Motivo de ultima hospitalizacion"),
         "padecimiento_actual" : fields.char("Padecimiento actual"),
         
         
         "sistema_digestivo" : fields.char("Sistema digestivo"),
         "sistema_respiratorio" : fields.char("Sistema respiratorio"),
         "sistema_cardiovascular" : fields.char("Sistema cardiovascular"),
         "aparato_genitourinario" : fields.char("Aparato genitourinario"),
         "sistema_endocrino" : fields.char("Sistema endocrino"),
         "sistema_hematopoyetico" : fields.char("Sistema hematopoyetico"),
         
         
         "frecuencia_cardiaca" : fields.float("Frecuencia cardiaca"),
         "frecuencia_respiratorio" : fields.float("Frecuencia respiratoria"),
         "tension_arterial" : fields.float("Tension arterial"),
         "temperatura" : fields.float("Temperatura"),
         
         
         "articulacion_mandibular" : fields.char("Articulacion Temporo Mandibular"),
         "ruidos" : fields.boolean("Ruidos"),
         "lateralidad" : fields.boolean("Lateralidad"),
         "apertura" : fields.boolean("Apertura"),
         "chasquidos" : fields.boolean("Chasquidos"),
         "tejidos_blandos" : fields.text("Tejidos blancos"),
         
         
         "gingivitis" : fields.char("Gingivitis"),
         "recesion_gingival" : fields.char("Recesion gingival"),
         "bolsas_periodontales" : fields.char("Bolsas periodontales"),
         "movilidad_dentaria" : fields.boolean("Movilidad dentaria"),
         "indice_pdb" : fields.float("Indice de PDB Actual"),
         "interpretacion_radiografica" : fields.text("Interpretacion radiografica"),
         
         
         "diagnostico" : fields.text("Diagnostico"),
         "alumno" : fields.char("Alumno"),
         "grupo" : fields.char("Grupo"),
        
    }
    
partner_clinica()