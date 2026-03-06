from odoo import http
from odoo.http import request, content_disposition


class UniversalReportController(http.Controller):

    @http.route([
        '/report/pdf/<string:reportname>',
        '/report/pdf/<string:reportname>/<string:docids>',
    ], type='http', auth='user')
    def report_pdf(self, reportname, docids=None, **data):

        report = request.env['ir.actions.report']._get_report_from_name(reportname)

        if docids:
            docids = [int(x) for x in docids.split(',')]
        else:
            docids = []

        # Compatible with old and new Odoo
        if hasattr(report, "_render_qweb_pdf"):
            pdf, _ = report._render_qweb_pdf(docids)
        else:
            pdf, _ = report.render_qweb_pdf(docids)

        headers = [
            ('Content-Type', 'application/pdf'),
            ('Content-Length', len(pdf)),
            ('Content-Disposition', content_disposition(f"{reportname}.pdf")),
        ]

        return request.make_response(pdf, headers=headers)
