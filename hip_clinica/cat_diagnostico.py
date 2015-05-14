# -*- coding: utf-8 -*-
from openerp.osv import osv, fields

class cat_diagnostico(osv.osv):
    
    _name = "cat.diagnostico"
    _columns = {
        "name" : fields.char("Clave"),
        "description" : fields.char("Descripcion"),
        "note" : fields.text("Notas"),        
    }
    
cat_diagnostico()