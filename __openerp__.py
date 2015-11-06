{
   'name': "Service report mass mailing",
    'version': '1.0',
    'depends': ['analytic','contract_report'],
    'author': "Bernard DELHEZ, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",
    'category': 'Sales',
    'description': 
    """
    Service report mass mailing

    It adds a new menuitem "Send by email" in the more section when your are in Contracts.
    It sends the service report for all selected contracts.
    
    This module has been developed by Bernard Delhez, intern @ AbAKUS it-solutions.
    """,
    'data': ['wizard/contract_report_mass_mailing.xml',
            ],
}