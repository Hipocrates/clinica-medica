# -*- coding: utf-8 -*-
from openerp.osv import osv, fields, expression

class cat_tratamiento(osv.osv):
    
    _name = "cat.tratamiento"
    _columns = { 
        "name" : fields.char("Clave"),
        "description" : fields.char("Descripcion"),
        "note" : fields.text("Notas"),
        "price" : fields.char("Precio"),
    }
    
    def name_search(self, cr, user, name, args=None, operator='ilike', context=None, limit=100):
        if not args:
            args = []
        args = args[:]
        ids = []

        if name:
            if operator not in expression.NEGATIVE_TERM_OPERATORS:
                ids = self.search(cr, user, ['|', ('description', '=like', name+"%"), ('name', operator, name)]+args, limit=limit)
                if not ids and len(name.split()) >= 2:
                    #Separating description and name of account for searching
                    operand1,operand2 = name.split(' ',1) #name can contain spaces e.g. OpenERP S.A.
                    ids = self.search(cr, user, [('description', operator, operand1), ('name', operator, operand2)]+ args, limit=limit)
            else:
                ids = self.search(cr, user, ['&','!', ('description', '=like', name+"%"), ('name', operator, name)]+args, limit=limit)
                # as negation want to restric, do if already have results
                if ids and len(name.split()) >= 2:
                    operand1,operand2 = name.split(' ',1) #name can contain spaces e.g. OpenERP S.A.
                    ids = self.search(cr, user, [('description', operator, operand1), ('name', operator, operand2), ('id', 'in', ids)]+ args, limit=limit)
        else:
            ids = self.search(cr, user, args, context=context, limit=limit)
        return self.name_get(cr, user, ids, context=context)
    
    def name_get(self, cr, uid, ids, context=None):
        if not ids:
            return []
        if isinstance(ids, (int, long)):
                    ids = [ids]
        reads = self.read(cr, uid, ids, ['description', 'name'], context=context)
        res = []
        for record in reads:
            name = record['description']
            if record['name']:
                name = record['name'] + ' ' + name
            res.append((record['id'], name))
        return res
    
cat_tratamiento()
