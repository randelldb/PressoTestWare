# 64bit required

import string

from django.http import HttpResponse
from weasyprint import HTML
from xhtml2pdf import pisa
import io as StringIO
from django.template.loader import get_template
from django.template import Context


def html_to_pdf_directly(request):
    template = get_template("test.html")
    context = Context({'pagesize': 'A4'})
    html = template.render(context)
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(StringIO.StringIO(html), dest=result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    else:
        return HttpResponse('Errors')


def pdf_generation():
    Html_template = get_template('test.html')
    pdf_file = HTML(Html_template).write_pdf()
    response = HttpResponse(pdf_file, content_type='mypdf.pdy')
    response['Content-Disposition'] = 'filename="home_page.pdf"'
    return response

pdf_generation()