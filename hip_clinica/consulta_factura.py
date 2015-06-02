from openerp.osv import osv, fields

class consulta_factura(osv.osv):

    _inherit = "account.invoice"
    
    _columns = {
        "alumno_id" : fields.many2one("alumnos", "Alumno"),
        "maestro_id" : fields.many2one("maestro", "Maestro"),
        "diagnostico" : fields.one2many("diagnostico", "diagnostico_factura", "Diagnostico"),
#         "tratamientos" : fields.one2many("plan.tratamiento.detalle", "factura_id", "Tratamiento"),
              
    }
    
consulta_factura()