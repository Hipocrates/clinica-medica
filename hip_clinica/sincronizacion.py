# -*- coding: utf-8 -*-
from openerp.osv import osv, fields
import time
import fdb
import sys, os

class sincronizacion(osv.osv):
    
    _name = "sincronizacion"
    def sincronizador(self, cr, uid, ids, context=None):
        
        path = os.path.abspath('/DB') + "\BDSISCUH.GDB"
        con = fdb.connect(dsn=path, user='SYSDBA', password='masterkey')
        cur = con.cursor()
        cur.execute("SELECT DISTINCT ALUMNOS.NOCONTROL, ALUMNOS.NOMBRE, SALONES.GRUPO, SALONES.PERIODO FROM ALUMNOS, MATERIAS, SALONES, CALIF WHERE ALUMNOS.NOCONTROL = CALIF.NOCONTROL AND MATERIAS.CLAVEMAT= SALONES.IDMATERIA AND CALIF.IDGPIF = SALONES.IDGPIF  AND SALONES.PERIODO='2014-2015' AND SALONES.GRUPO LIKE '%ODM%' ORDER BY ALUMNOS.NOMBRE")
        rows = cur.fetchall()
        cur.execute("SELECT DISTINCT ALUMNOS.NOCONTROL, ALUMNOS.NOMBRE, SALONES.GRUPO, SALONES.PERIODO FROM ALUMNOS, MATERIAS, SALONES, CALIF WHERE ALUMNOS.NOCONTROL = CALIF.NOCONTROL AND MATERIAS.CLAVEMAT= SALONES.IDMATERIA AND CALIF.IDGPIF = SALONES.IDGPIF  AND SALONES.PERIODO='2014-2015' AND SALONES.GRUPO LIKE '%MEM%' ORDER BY ALUMNOS.NOMBRE")
        rows2 = cur.fetchall()
        cur.execute("SELECT DISTINCT ALUMNOS.NOCONTROL, ALUMNOS.NOMBRE, SALONES.GRUPO, SALONES.PERIODO FROM ALUMNOS, MATERIAS, SALONES, CALIF WHERE ALUMNOS.NOCONTROL = CALIF.NOCONTROL AND MATERIAS.CLAVEMAT= SALONES.IDMATERIA AND CALIF.IDGPIF = SALONES.IDGPIF  AND SALONES.PERIODO='2014-2015' AND SALONES.GRUPO LIKE '%MOM%' ORDER BY ALUMNOS.NOMBRE")
        rows3 = cur.fetchall()
        cur.execute("SELECT DISTINCT ALUMNOS.NOCONTROL, ALUMNOS.NOMBRE, SALONES.GRUPO, SALONES.PERIODO FROM ALUMNOS, MATERIAS, SALONES, CALIF WHERE ALUMNOS.NOCONTROL = CALIF.NOCONTROL AND MATERIAS.CLAVEMAT= SALONES.IDMATERIA AND CALIF.IDGPIF = SALONES.IDGPIF  AND SALONES.PERIODO='2014-2015' AND SALONES.GRUPO LIKE '%INH%' ORDER BY ALUMNOS.NOMBRE")
        rows4 = cur.fetchall()
        alumno_obj = self.pool.get("alumnos")
        
        for row in rows:
            
            vals = {
                "matricula" : row[0].strip(),
                "nombre" : row[1].strip().replace(";", " "),
                "grupo" : row[2],
                "ciclo" : row[3],
                "especialidad" : "odontologia"
            }
            
            domain=[('matricula', '=', vals['matricula'])]
            
            alumno_idsearch = alumno_obj.search(cr, uid, domain)
            
            if alumno_idsearch:
                """ esto es una lista [1,2,3]"""
                alumno_obj.write(cr, uid, alumno_idsearch, vals, context)
            else:
                """ Devuelve []"""
                alumno_id = alumno_obj.create(cr, uid, vals, context)
                
        for row in rows2:
                
                
            vals = {
                "matricula" : row[0].strip(),
                "nombre" : row[1].strip().replace(";", " "),
                "grupo" : row[2],
                "ciclo" : row[3],
                "especialidad" : "espendodoncia"
            }
            
            domain=[('matricula', '=', vals['matricula'])]
            
            alumno_idsearch = alumno_obj.search(cr, uid, domain)
            
            if alumno_idsearch:
                """ esto es una lista [1,2,3]"""
                alumno_obj.write(cr, uid, alumno_idsearch, vals, context)
            else:
                """ Devuelve []"""
                
                alumno_id = alumno_obj.create(cr, uid, vals, context)
                
                
        for row in rows3:
                
                
            vals = {
                "matricula" : row[0].strip(),
                "nombre" : row[1].strip().replace(";", " "),
                "grupo" : row[2],
                "ciclo" : row[3],
                "especialidad" : "esportodoncia"
            }
            
            domain=[('matricula', '=', vals['matricula'])]
            
            alumno_idsearch = alumno_obj.search(cr, uid, domain)
            
            if alumno_idsearch:
                """ esto es una lista [1,2,3]"""
                alumno_obj.write(cr, uid, alumno_idsearch, vals, context)
            else:
                """ Devuelve []"""
                
                alumno_id = alumno_obj.create(cr, uid, vals, context)
                
        for row in rows4:                
                
            vals = {
                "matricula" : row[0].strip(),
                "nombre" : row[1].strip().replace(";", " "),
                "grupo" : row[2],
                "ciclo" : row[3],
                "especialidad" : "esprehabilitacion"
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
        
        path = os.path.abspath('/DB') + "\BDSISCUH.GDB"
        con = fdb.connect(dsn=path, user='SYSDBA', password='masterkey')
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
