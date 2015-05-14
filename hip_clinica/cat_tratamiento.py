# -*- coding: utf-8 -*-
from openerp.osv import osv, fields

class cat_tratamiento(osv.osv):
    
    _name = "cat.tratamiento"
    _columns = {
        "name" : fields.char("Clave"),
        "description" : fields.char("Descripcion"),
        "note" : fields.text("Notas"),
        "price" : fields.char("Precio"),
    }
    
cat_tratamiento()
