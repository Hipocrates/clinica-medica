# -*- coding: utf-8 -*-
{
    'name': 'Modulo Clinica',
    'version': '1.0.0',
    'category': 'Medicine',
    'sequence': 1,
    'author': 'Gerardo A Lopez Vega @glopzvega',
    'website': 'http://www.uhipocrates.com',
    'summary': 'Modulo Clinica',
    'description': "Este modulo es para administracion de la clinica",
    'depends': ["sale"],
    'data': [
             "menu.xml",
             "hip_alumnos_view.xml",
             "hip_maestro_view.xml", 
             "hip_consulta_view.xml",
            "cat_diagnostico_view.xml", 
            "cat_tratamiento_view.xml",  
            "diagnostico_view.xml", 

             "plan_tratamiento_detalle_view.xml",              
             "consulta_factura_view.xml",
             "sincronizacion_view.xml",
             ],    
    'installable': True,
    'active': False
}