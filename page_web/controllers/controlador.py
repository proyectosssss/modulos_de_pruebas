# -*- coding: utf-8 -*-
import logging
import odoo.http as http
logger = logging.getLogger(__name__)

class your_class(http.Controller):
     @http.route('/page1', type='http', auth='user', website=True)
     def show_custom_webpage(self, **kw):
          return http.request.render('page_web.page1', {})



