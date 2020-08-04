from odoo import models, api, fields


class SalesDiscount(models.Model):
    _inherit = 'sale.order'
    _description = 'Sale order inherit '

    customer_discount_code = fields.Text(string="Discount code", related='partner_id.customer_discount_code', readonly=True)
    valid_code = fields.Char(string='Checked code', related='partner_id.valid_code', readonly=True)

    sale_order_discount_estimated = fields.Monetary(string="Discount Total ", store=True,compute='estimate_discount_total' ,readonly=True)
    # sale_order_customer_discount = fields.Char(string='Customer Discount', default='0.00', readonly=True)




    @api.depends('amount_total', 'partner_id', 'customer_discount_code', 'sale_order_template_id')
    def  estimate_discount_total(self):
        for rec in self:
            if(rec.valid_code == 'Invalid code"'):
                rec.sale_order_discount_estimated = rec.amount_total
                rec.note = ""

            elif(rec.valid_code =='Valid code'):
                discount_code = rec.customer_discount_code.split('_')
                discount_val = int(discount_code[1])
                rec.note = "The Sale Order was discount "+ discount_code[1] +"% by code: "+rec.partner_id.customer_discount_code
                rec.sale_order_discount_estimated  = rec.amount_total - (discount_val/100 * rec.amount_total)

