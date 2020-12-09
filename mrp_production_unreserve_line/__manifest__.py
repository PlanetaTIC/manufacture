# Copyright 2020 PlanetaTIC - Marc Poch <mpoch@planetatic.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


{
    'name': 'MRP Production Unreserve Line',
    'summary': 'Permits to unreserve lines of mrp production',
    'version': '12.0.1.0.0',
    'category': 'Stock',
    'author': 'PlanetaTIC'
              ' Odoo Community Association (OCA)',
    'website': 'https://github.com/OCA/manufacture',
    'license': 'AGPL-3',
    'depends': [
        'mrp',
        'stock_picking_unreserve_line',
    ],
    'data': [
        'views/stock_move_views.xml',
    ],
    'installable': True,
    'auto_install': False
}
