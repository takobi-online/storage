# Copyright 2018 Akretion (http://www.akretion.com).
# @author Pierrick Brun <https://github.com/pierrickbrun>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    "name": "Storage Image Product POS",
    "summary": "Link images to products and categories inside POS",
    "version": "14.0.1.0.1",
    "category": "Storage",
    "website": "https://github.com/OCA/storage",
    "author": " Akretion, Odoo Community Association (OCA)",
    "license": "LGPL-3",
    "installable": False,
    "depends": ["storage_image_product", "point_of_sale"],
    "data": ["views/pos_product.xml"],
    "maintainers": ["hparfr", "pierrickbrun"],
}
