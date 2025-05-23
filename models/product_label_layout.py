# product_labeling/models/product_label_layout.py
from odoo import _, api, fields, models
from odoo.exceptions import UserError
from dateutil.relativedelta import relativedelta


class ProductLabelLayout(models.TransientModel):
    _inherit = "product.label.layout"

    print_format = fields.Selection(
        selection_add=[
            ("eti_corta", "ETI-CORTA"),
            ("eti_media", "ETI-MEDIA"),
            ("eti_larga", "ETI-LARGA"),
            ("eti_caja", "ETI-CAJA"),
        ],
        string="Formato",
        ondelete={
            "eti_corta": "set default",
            "eti_media": "set default",
            "eti_larga": "set default",
            "eti_caja": "set default",
        },
    )
    lot_name = fields.Char(
        string="Número de Lote", compute="_compute_lot_info", store=True
    )
    manufacturing_date = fields.Date(
        string="Fecha de Fabricación", compute="_compute_lot_info", store=True
    )
    expiration_date = fields.Date(
        string="Fecha de Vencimiento", compute="_compute_lot_info", store=True
    )

    @api.depends("custom_quantity")
    def _compute_lot_info(self):
        for wizard in self:
            if (
                "active_model" in self._context
                and self._context["active_model"] == "mrp.production"
            ):
                production = self.env["mrp.production"].browse(
                    self._context.get("active_id")
                )
                wizard.lot_name = (
                    production.lot_producing_id.name
                    if production.lot_producing_id
                    else ""
                )
                wizard.manufacturing_date = production.date_start or fields.Date.today()
                wizard.expiration_date = (
                    wizard.manufacturing_date + relativedelta(years=2)
                    if wizard.manufacturing_date
                    else False
                )
            else:
                wizard.lot_name = ""
                wizard.manufacturing_date = False
                wizard.expiration_date = False

    @api.onchange("product_ids")
    def _onchange_product_ids(self):
        if self._context.get("active_model") == "mrp.production":
            production = self.env["mrp.production"].browse(
                self._context.get("active_id")
            )
            self.product_ids = [(6, 0, [production.product_id.id])]
            self.custom_quantity = production.product_qty
            self.move_quantity = "custom"

    def _generate_zpl_eti_corta(self, production):
        zpl = ""
        # 104mm x 61mm, 1mm ≈ 8 dots, 104mm = 832 dots, 61mm = 488 dots
        for _ in range(int(self.custom_quantity)):
            zpl += """
            ^XA^CI28
            ^PW832^LH0,0
            ^FT50,40^A0N,30,24^FDKFP S.A.^FS
            ^FT150,100^A0N,40,30^FD{product_name}^FS
            ^FT150,140^A0N,30,24^FD{lot_number}^FS
            ^FT150,180^A0N,30,24^FD{manufacturing_date}^FS
            ^FT150,220^A0N,30,24^FD{expiration_date}^FS
            ^XZ
            """.format(
                product_name=production.product_id.name,
                lot_number=production.lot_producing_id.name or "",
                manufacturing_date=production.date_start or fields.Date.today(),
                expiration_date=(production.date_start + relativedelta(years=2))
                if production.date_start
                else "",
            )
        return zpl

    def _generate_zpl_eti_media(self, production):
        zpl = ""
        # 109mm x 149mm, 109mm = 872 dots, 149mm = 1192 dots
        for _ in range(int(self.custom_quantity)):
            zpl += """
            ^XA^CI28
            ^PW872^LH0,0
            ^FT50,40^A0N,30,24^FDKFP S.A.^FS
            ^FT150,100^A0N,40,30^FD{product_name}^FS
            ^FT150,140^A0N,30,24^FD{lot_number}^FS
            ^FT150,180^A0N,30,24^FD{manufacturing_date}^FS
            ^FT150,220^A0N,30,24^FD{expiration_date}^FS
            ^XZ
            """.format(
                product_name=production.product_id.name,
                lot_number=production.lot_producing_id.name or "",
                manufacturing_date=production.date_start or fields.Date.today(),
                expiration_date=(production.date_start + relativedelta(years=2))
                if production.date_start
                else "",
            )
        return zpl

    def _generate_zpl_eti_larga(self, production):
        zpl = ""
        # 66mm x 251mm, 66mm = 528 dots, 251mm = 2008 dots
        for _ in range(int(self.custom_quantity)):
            zpl += """
            ^XA^CI28
            ^PW528^LH0,0
            ^FT50,40^A0N,30,24^FDKFP S.A.^FS
            ^FT150,100^A0N,40,30^FD{product_name}^FS
            ^FT150,140^A0N,30,24^FD{lot_number}^FS
            ^FT150,180^A0N,30,24^FD{manufacturing_date}^FS
            ^FT150,220^A0N,30,24^FD{expiration_date}^FS
            ^XZ
            """.format(
                product_name=production.product_id.name,
                lot_number=production.lot_producing_id.name or "",
                manufacturing_date=production.date_start or fields.Date.today(),
                expiration_date=(production.date_start + relativedelta(years=2))
                if production.date_start
                else "",
            )
        return zpl

    def _generate_zpl_eti_caja(self, production):
        zpl = ""
        # 109mm x 149mm, 109mm = 872 dots, 149mm = 1192 dots
        for _ in range(int(self.custom_quantity)):
            zpl += """
            ^XA^CI28
            ^PW872^LH0,0
            ^FT50,40^A0N,30,24^FDKFP S.A.^FS
            ^FT150,100^A0N,40,30^FD{product_name}^FS
            ^FT150,140^A0N,30,24^FD{lot_number}^FS
            ^FT150,180^A0N,30,24^FD{manufacturing_date}^FS
            ^FT150,220^A0N,30,24^FD{expiration_date}^FS
            ^XZ
            """.format(
                product_name=production.product_id.name,
                lot_number=production.lot_producing_id.name or "",
                manufacturing_date=production.date_start or fields.Date.today(),
                expiration_date=(production.date_start + relativedelta(years=2))
                if production.date_start
                else "",
            )
        return zpl

    def _prepare_report_data(self):
        if self.print_format in ["eti_corta", "eti_media", "eti_larga", "eti_caja"]:
            if self.custom_quantity <= 0:
                raise UserError(_("You need to set a positive quantity."))

            if (
                "active_model" not in self._context
                or self._context["active_model"] != "mrp.production"
            ):
                raise UserError(
                    _(
                        "Este tipo de etiqueta solo puede usarse desde una orden de fabricación."
                    )
                )

            production = self.env["mrp.production"].browse(
                self._context.get("active_id")
            )
            if not production.lot_producing_id:
                raise UserError(
                    _("La orden de fabricación debe tener un lote asignado.")
                )

            # Generar ZPL según el tipo de etiqueta
            if self.print_format == "eti_corta":
                zpl_data = self._generate_zpl_eti_corta(production)
            elif self.print_format == "eti_media":
                zpl_data = self._generate_zpl_eti_media(production)
            elif self.print_format == "eti_larga":
                zpl_data = self._generate_zpl_eti_larga(production)
            elif self.print_format == "eti_caja":
                zpl_data = self._generate_zpl_eti_caja(production)

            # Crear un archivo temporal para el ZPL y devolver una acción para descargarlo
            import base64

            zpl_file = base64.b64encode(zpl_data.encode("utf-8"))
            attachment = self.env["ir.attachment"].create(
                {
                    "name": f"etiqueta_{self.print_format}.zpl",
                    "datas": zpl_file,
                    "type": "binary",
                }
            )

            return {
                "type": "ir.actions.act_url",
                "url": f"/web/content/{attachment.id}?download=true",
                "target": "self",
                "close_on_report_download": True,
            }

        # Flujo original para otros formatos
        return super(ProductLabelLayout, self)._prepare_report_data()
