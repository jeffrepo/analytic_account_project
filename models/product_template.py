# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _


class ProductTemplate(models.Model):
    _inherit = "product.template"

    create_analytic_sale = fields.Boolean('Crear movimiento analitico en venta')
