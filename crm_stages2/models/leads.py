# -*- coding:utf-8 -*-
import logging
from odoo import fields, models, api
logger = logging.getLogger(__name__)
from odoo import api, fields, models, tools, SUPERUSER_ID

class Leads(models.Model):
    _inherit = 'crm.lead'

    @api.model
    def _read_group_stage_ids_2(self,stages,domain,order):
        stage_ids = self.env['new.stage'].search([])
        return stage_ids

    type_lead_custom = fields.Selection(
        [('a', 'a'),
         ('b', 'b')
         ], string='Oportunity Type')

   
    new_stage_id = fields.Many2one('new.stage',readonly=False ,string="New Stage",group_expand='_read_group_stage_ids_2')
    
    @api.onchange('type_lead_custom')
    def _onchange_(self):
        if self.type_lead_custom == 'b':
            self.new_stage_id = self.env['new.stage'].search([('name','=','Identify')],limit=1)
            self.stage_id = False
        else:
            self.stage_id = self.env['crm.stage'].search([('name','=','New')],limit=1)
            self.new_stage_id = False
    
    
            
    
     
    
    

    

    
    
  
