# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import AccessError, UserError

class AchInventoryReport(models.TransientModel):
    _name = 'ach.inventory.report'

    name = fields.Char(string="Name")
    date = fields.Date(string="Date")
    type = fields.Selection([('general','General'),('location','Location'),('warehouse','Warehouse'),('product','Product')], string="Type", default='general')
    company_id = fields.Many2one('res.company', string="Company", default=lambda self: self.env.user.company_id.id)
    location_id = fields.Many2one('stock.location',string="Location")
    warehouse_id = fields.Many2one('stock.warehouse', string="Warehouse")
    product_id = fields.Many2one('product.product', string="Product")