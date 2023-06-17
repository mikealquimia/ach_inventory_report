# -*- coding: utf-8 -*-
import json
import io
try:
    from odoo.tools.misc import xlsxwriter
except ImportError:
    import xlsxwriter
from odoo import api, fields, models, tools, SUPERUSER_ID
from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta
from decimal import Decimal, ROUND_HALF_UP
import logging
_logger = logging.getLogger(__name__)

class AcgInventoryReportXlsx(models.AbstractModel):
    _name = 'report.ach_inventory_report.xlsx_inventory_report'
    _inherit = 'report.report_xlsx.abstract'
    _description = "Inventory Report"

    def generate_xlsx_report(self, workbook, data, lines):
        sheet = workbook.add_worksheet('Test')
        type_report = lines.type
        product_id = lines.product_id
        location_id = lines.location_id
        warehouse = lines.warehouse_id
        company_id = lines.company_id
        date = lines.date
        data_left = workbook.add_format({'font_name': 'Arial', 'bold': False, 'font_size': 10, 'font_color': 'black', 'align': 'left', 'right': 1, 'left': 1, 'top': 1, 'bottom': 1, 'valign': 'vcenter'})
        data_right = workbook.add_format({'font_name': 'Arial', 'bold': False, 'font_size': 10, 'font_color': 'black', 'align': 'right', 'right': 1, 'left': 1, 'top': 1, 'bottom': 1, 'valign': 'vcenter', 'num_format': '#,##0.00'})
        data_right_alert = workbook.add_format({'font_name': 'Arial', 'bold': False, 'font_size': 10, 'font_color': 'red', 'align': 'right', 'right': 1, 'left': 1, 'top': 1, 'bottom': 1, 'valign': 'vcenter', 'num_format': '#,##0.00'})
        if type_report == 'general':
            self.env.cr.execute("""
select pt.default_code as code, pt.name as product, sum(sq.quantity) as qty, uu.name as uom 
from product_product pp 
inner join stock_location sl 
on sl.usage = 'internal' 
inner join stock_quant sq 
on sq.product_id  = pp.id 
and sq.location_id = sl.id 
inner join product_template pt 
on pt.id = pp.product_tmpl_id 
inner join uom_uom uu 
on uu.id = pt.uom_id 
group by pt.default_code, pt.name, uu.name
order by pt.default_code 
            """)
            row_index = 4
            sheet.write('B3', 'Code', data_left)
            sheet.write('C3', 'Product', data_left)
            sheet.write('D3', 'Qty', data_left)
            sheet.write('E3', 'Uom', data_left)
            for line in self.env.cr.dictfetchall():
                sheet.write('B'+str(row_index), line['code'], data_left)
                sheet.write('C'+str(row_index), line['product'], data_left)
                sheet.write('D'+str(row_index), line['qty'], data_right if line['qty'] > 0 else data_right_alert)
                sheet.write('E'+str(row_index), line['uom'], data_left)
                row_index += 1
        workbook.close()