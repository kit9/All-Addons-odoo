{
    'version': '0.2',
    'name': 'Aplikasi e-Office',
    'depends': ['base','mail'],
    'author'  :'asopkarawang@gmail.com',
    'category': 'Other',
    'data': [
        'view/eo_menu.xml',
        'view/doc.xml',
        'view/doc_template.xml',
        'data/ir_sequence.xml',
        'data/doc_type.xml',
    	'data/doc_template.xml',
        'security/ir.model.access.csv',
        'security/record_rules.xml',
        'reports/doc_report_menu.xml',
        'reports/doc.xml',
    ],    
    'description': """
Description
==================
aplikasi e-office

""",
    'installable':True,

}