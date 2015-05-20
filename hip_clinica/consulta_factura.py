from openerp.osv import osv, fields

class consulta_factura(osv.osv):

    _inherit = "account.invoice"
    
    _columns = {
        "alumno_id" : fields.many2one("alumnos", "Alumno"),
        "maestro_id" : fields.many2one("maestro", "Maestro"),
              
    }
    
consulta_factura()