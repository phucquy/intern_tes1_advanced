
from odoo import  models, api, fields
import re
class CustomerDiscount(models.Model):
    _inherit = 'res.partner'
    _description = 'Res Partner Inherit'

    customer_discount_code = fields.Text(string="Discount code")
    valid_code = fields.Char(string='Status', compute='check_discount_code',store=True)

    @api.depends('customer_discount_code')
    def check_discount_code(self):
        # print('check '+str(self.valid_code))
        for rec in self:
            if (not rec.customer_discount_code):
                rec.valid_code = "Invalid code"
            else:
                if(re.match("^VIP_([1-9]|[1-9][0-9]|0[1-9])$", rec.customer_discount_code)):
                    rec.valid_code = "Valid code"
                else:
                    rec.valid_code = "Invalid code"


