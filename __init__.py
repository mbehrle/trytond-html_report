# This file is part html_report module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from trytond.report import Report
from . import action
from . import translation
from . import html
from . import engine
from . import invoice
from . import production
from . import purchase
from . import sale
from . import sale_product_customer
from . import stock

def register():
    module = 'html_report'
    Pool.register(
        action.ActionReport,
        action.HTMLTemplateTranslation,
        html.Signature,
        html.Template,
        html.TemplateUsage,
        html.ReportTemplate,
        module=module, type_='model')
    Pool.register(
        translation.ReportTranslationSet,
        module=module, type_='wizard')
    Pool.register_mixin(engine.HTMLReportMixin, Report,
        module=module)

    invoice.register(module)
    production.register(module)
    purchase.register(module)
    sale.register(module)
    sale_product_customer.register(module)
    stock.register(module)
