# Copyright 2016 Tecnativa - Jairo Llopis
# Copyright 2017 Tecnativa - Pedro M. Baeza
# Copyright 2019 ForgeFlow S.L. - Lois Rilo <lois.rilo@forgeflow.com>
# 2020 NextERP Romania
# Copyright 2021 Tecnativa - João Marques
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Mail Debrand",
    "summary": "Remove Odoo branding links from outgoing emails.",
    "description": """
Removes Odoo branding links from rendered outgoing emails while preserving the original message body content.
    """,
    "version": "18.0.1.0.1",
    "category": "Productivity",
    "website": "https://nextpagetechnologies.com",
    "author": "Next Page Technologies Pvt Ltd",
    "license": "AGPL-3",
    "installable": True,
    "depends": ["mail"],
    "images": [
        "static/description/banner.png",
    ],
}
