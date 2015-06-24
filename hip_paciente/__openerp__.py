# -*- coding: utf-8 -*-
{
    'name' : 'Clinica',
    'version' : '1.1',
    'sequence' : '1',
    'author' : 'OpenERP SA',
    'category' : 'Administracion',
    'description' : """
Pacientes de la Universidad Hipocrates.
====================================
""",
    'website': 'http://uhipocrates.edu.mx',
    'depends' : ['hip_clinica'],
    'data': [
             "hip_paciente_view.xml",
             "menu.xml",
             ],
    'installable': True,    
    'active' : False
}
