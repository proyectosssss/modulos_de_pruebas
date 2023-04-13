# -*- coding:utf-8 -*-

{
    'name': 'marketingAutomation',
    'depends': ['base','contacts','marketing_automation'],
    'data':['views/views.xml','views/actions.xml','security/ir.model.access.csv','security/securityxml.xml'],
    'description':
     """

     This is a module to add a new functionality to marketing.campaign model.
     There are 2 things added:
        1: new features at contact module (new model called campaign, new form features at res.partner model).
        2: new features at marketing.campaign model (python logic, form features).

     Details:
        1: We have created a new model in contact module that is called campaign.
           This campaign have a many2many field related to res.partner model, and few fields with some details about the campaign.
        2: We have added a new tab in res.partner model with a many2many field related to the campaign model.
        3: We have created a many2one field in marketing.campaign model pointing to campaign model.
        4: We have added some logic (method) to relate the contacts in the real campaigns from marketing.campaign model 
           with the campaign from contact module.

     """,
}