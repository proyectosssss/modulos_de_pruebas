# -*- coding: utf-8 -*-

import logging
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal

logger = logging.getLogger(__name__)
class PortalAccount(CustomerPortal):
     def _prepare_home_portal_values(self, counters):
          values = super()._prepare_home_portal_values(counters)
          #values['product_product_stock_tree'] = request.env['product.product'].search_count([])
          return values

