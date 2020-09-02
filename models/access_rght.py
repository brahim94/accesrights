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
 
