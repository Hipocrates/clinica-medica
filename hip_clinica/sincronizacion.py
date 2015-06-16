# -*- coding: utf-8 -*-
from openerp.osv import osv, fields
import time
import fdb

class sincronizacion(osv.osv):
    
    _name = "sincronizacion"
    def sincronizador(self, cr, uid, ids, context=None):   
        
        con = fdb.connect(dsn='C:\Osvaldo\BDSISCUH.GDB', user='SYSDBA', password='masterkey')
        cur = con.cursor()
        cur.execute("SELECT DISTINCT ALUMNOS.NOCONTROL, ALUMNOS.NOMBRE, SALONES.GRUPO, SALONES.PERIODO FROM ALUMNOS, MATERIAS, SALONES, CALIF WHERE ALUMNOS.NOCONTROL = CALIF.NOCONTROL AND MATERIAS.CLAVEMAT= SALONES.IDMATERIA AND CALIF.IDGPIF = SALONES.IDGPIF  AND SALONES.PERIODO='2014-2015' AND SALONES.GRUPO LIKE '%ODM%' ORDER BY ALUMNOS.NOMBRE")
        rows = cur.fetchall()
        
        alumno_obj = self.pool.get("alumnos")
        
        for row in rows:
            
            
            vals = {
                "matricula" : row[0].strip(),
                "nombre" : row[1].strip().replace(";", " "),
                "grupo" : row[2],
                "ciclo" : row[3],
            }
            
            domain=[('matricula', '=', vals['matricula'])]
            
            alumno_idsearch = alumno_obj.search(cr, uid, domain)
            
            if alumno_idsearch:
                """ esto es una lista [1,2,3]"""
                alumno_obj.write(cr, uid, alumno_idsearch, vals, context)
            else:
                """ Devuelve []"""
                alumno_id = alumno_obj.create(cr, uid, vals, context)
            print vals
        return True
    
    def sincromaestro(self, cr, uid, ids, context=None):   
        
        con = fdb.connect(dsn='C:\Osvaldo\BDSISCUH.GDB', user='SYSDBA', password='masterkey')
        cur = con.cursor()
        cur.execute("select NOMBRE, CHECADOR  from PROFESORES WHERE CHECADOR is not null")
        rows = cur.fetchall()
        
        maestro_obj = self.pool.get("maestro")
        
        for row in rows:
            
            vals = {
                "nombre" : row[0].strip().replace(";", " "),
                "cedula" : row[1].strip(),
            }
            maestro_id = maestro_obj.create(cr, uid, vals, context)
            print vals
    
sincronizacion()
