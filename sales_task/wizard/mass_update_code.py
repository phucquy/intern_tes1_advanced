from odoo import api, models, fields


class MassUpdateCode(models.TransientModel):
    _name = 'mass.update.code'

    _description = 'Mass Update Customer Code'

    customer_discount_code = fields.Text(string="Discount code")

    def update(self):
        list = self.env['res.partner'].browse(self._context['active_ids'])
        for rec in list:
            rec.customer_discount_code = self.customer_discount_code
            # print(rec)