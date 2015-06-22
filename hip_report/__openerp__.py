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
    'depends': ["hip_clinica"],
    'data': [             
             "report_invoice.xml",
             "invoice_report.xml",
             "report_extraccion.xml",
             "extraccion_report.xml",
             "evolucion_report.xml",
             "report_evolucion.xml",
             
             ],    
    'installable': True,
    'active': False
}