# -*- coding: utf-8 -*-
from openerp.osv import osv, fields
from hip_clinica.receta import receta

class receta_detalle(osv.osv):
    
    _name = "receta.detalle"
    _columns = {
        "id_receta_detalle" : fields.integer("Clavereceta detalle"),
        "id_receta" : fields.many2one("receta", "Receta"),
        "medicamento" : fields.char("Medicamento"),
        "indicaciones" : fields.char("Indicaciones"),
    }
receta_detalle()