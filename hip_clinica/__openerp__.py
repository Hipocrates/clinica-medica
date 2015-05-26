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
             "hip_plan_tratamiento_view.xml",
             
             "cat_diagnostico_view.xml", 
             "menu_cat_diagnostico.xml", 
             "cat_tratamiento_view.xml", 
             "menu_cat_tratamiento.xml", 
             "diagnostico_view.xml", 
             "menu_diagnostico.xml",
             
             "diagnostico_detalle_view.xml", 
             "menu_diagnostico_detalle.xml", 
             "receta_view.xml", 
             "menu_receta.xml",
             
             "receta_detalle_view.xml", 
             "menu_receta_detalle.xml", 
             "pago_view.xml", 
             "menu_pago.xml", 
             "consulta_view.xml",
             "menu_consulta.xml", 
               
             "consulta_factura_view.xml"
             ],    
    'installable': True,
    'active': False
}