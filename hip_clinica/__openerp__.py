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
    'data': ["cat_diagnostico_view.xml", "menu_cat_diagnostico.xml", "cat_tratamiento_view.xml", "menu_cat_tratamiento.xml", "diagnostico_view.xml", "menu_diagnostico.xml",
             "plan_tratamiento_view.xml","menu_plan_tratamiento.xml", "plan_tratamiento_detalle_view.xml","menu_plan_tratamiento_detalle.xml",
             "diagnostico_detalle_view.xml", "menu_diagnostico_detalle.xml", "receta_view.xml", "menu_receta.xml", "alumnos_view.xml", "menu_alumnos.xml",
              "receta_detalle_view.xml", "menu_receta_detalle.xml", "pago_view.xml", "menu_pago.xml", "consulta_view.xml", "menu_consulta.xml", "maestro_view.xml", "menu_maestro.xml",  "consulta_factura_view.xml"],    
    'installable': True,
    'active': False
}