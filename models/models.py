# -*- coding: utf-8 -*-

from odoo import models, fields, api


class NotasVenta(models.Model):
    _inherit = 'sale.order'

    @api.multi
    def action_confirm(self):
        super(NotasVenta,self).action_confirm()
        if self.opportunity_id:
            oportunidad=self.opportunity_id
            oportunidad.action_set_won_rainbowman()
            estado_ganado=self.env['crm.stage'].search([('name','=','Ganado')],limit=1)
            oportunidad.stage_id= estado_ganado.id
