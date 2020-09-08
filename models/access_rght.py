from odoo import fields, api, models, _

class magasin(models.Model): 
    _inherit = "crm.magasin"

    id_magasin = fields.Char(string="ID magasin", required="True")
    _sql_constraints = [
        ('name_uniq',
         'UNIQUE (id_magasin)',
         'id magasin must be unique.')
    ]

class ResUsers(models.Model):
    _inherit = "res.users"

    all_stores = fields.Boolean(string="Tous les magasins")
    magasin_ids = fields.Many2many('crm.magasin', 'magasins_user_rel', 'user_id', 'magasin_id', string='Magasins associés')


class aftersales(models.Model):
    _inherit = "ticket.ticket"

    business_unit = fields.Many2one('crm.team', string='BU')
    magasin = fields.Many2one('crm.magasin', string='Magasin')

    @api.onchange('client_id')
    def onchange_client_id(self):
        self.business_unit = self.client_id.business_unit_id
        self.magasin = self.client_id.magasin_id


class Factures(models.Model):
    _inherit = "factures.factures"

    magasin = fields.Many2one('crm.magasin', string='Magasin')
    magasin_id = fields.Char(related='magasin.id_magasin', string='Magasin ID')
