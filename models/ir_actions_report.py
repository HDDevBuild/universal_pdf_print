from odoo import models


class IrActionsReport(models.Model):
    _inherit = "ir.actions.report"

    def _check_report_wkhtmltopdf(self):
        """
        Override the worker check that blocks PDF printing
        when workers < 2
        """
        return True
