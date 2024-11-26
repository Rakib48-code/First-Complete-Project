{
    'name': 'Rakib Hospital Management',
    'version': '1.0.0',
    'summary': 'A module for managing hospital operations including patients, doctors, and appointments.',
    'description': 'This module helps manage various hospital activities such as patient records, doctor schedules, appointments, billing, and more.',
    'author': 'Rakib Hasan',
    'category': 'Healthcare',
    'depends': ['base'],  # Add any other dependencies your module might need
    'data': [
        # Add paths to your XML or CSV files
        'security/ir.model.access.csv',  # Security rules
        'views/menu_view.xml',     # Menu views
        'views/patient_view.xml',  # Patient views
        #'views/doctor_view.xml',  # Doctor views
        'views/appointment_view.xml',  # Appointment views
        #'data/default_data.xml',  # Default data
    ],
    'demo': [
        # Add demo data files if any
        'demo/demo_data.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
