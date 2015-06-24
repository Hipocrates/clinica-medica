# -*- coding: utf-8 -*-
from openerp.osv import osv, fields

class res_company(osv.osv):

    _inherit = "res.company"
    
    _columns = {  
                "hip_header" : fields.binary("Encabezado"),
                "hip_footer" : fields.binary("Pie de pagina"),
    }
    
res_company()