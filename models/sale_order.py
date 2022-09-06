# -*- coding: utf-8 -*-

from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import AccessError, UserError, ValidationError
import datetime
import logging

class SaleOrder(models.Model):
    _inherit = "sale.order"

    def action_confirm(self):
        for sale in self:
            logging.warning(sale.analytic_account_id)
            if sale.analytic_account_id and sale.order_line:
                for line in sale.order_line:
                    logging.warning(line.product_id.create_analytic_sale)
                    if line.product_id.create_analytic_sale:
                        analytic_move_dic = {'name': sale.name, 'account_id': sale.analytic_account_id.id, 'date': datetime.date.today(), 'amount': line.product_id.standard_price * -1, 'product_id': line.product_id.id }
                        analytic_move_id = self.env['account.analytic.line'].create(analytic_move_dic)
                        logging.warning(analytic_move_id)
        return super(SaleOrder, self).action_confirm()

    def action_cancel(self):
        for sale in self:
            logging.warning(sale.analytic_account_id)
            if sale.analytic_account_id and sale.order_line:
                analytic_moves = self.env['account.analytic.line'].search([('account_id','=',sale.analytic_account_id.id),('product_id.create_analytic_sale','=',True)])
                if analytic_moves:
                    analytic_moves.unlink()
        return super(SaleOrder, self).action_cancel()
