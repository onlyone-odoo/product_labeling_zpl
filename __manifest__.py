# product_labeling/__manifest__.py
{
    "name": "Product Labeling",
    "summary": """
        Módulo para generar etiquetas ZPL personalizadas (ETI-CORTA, ETI-MEDIA, ETI-LARGA, ETI-CAJA) desde órdenes de fabricación en MRP.""",
    "author": "Be OnlyOne",
    "maintainers": ["onlyone-odoo"],
    "website": "https://onlyone.odoo.com/",
    "license": "AGPL-3",
    "category": "Technical Settings",
    "version": "17.0.1.0.0",
    "development_status": "Production/Stable",
    "application": False,
    "installable": True,
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "depends": ["base", "product", "stock", "mrp"],
    "data": [
        "views/product_label_layout_views.xml",
    ],
}
