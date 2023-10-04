import base64
import json

import requests
from celery import shared_task
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.template.loader import get_template

from service_app.models import Check


@shared_task
def create_pdf(check_id):
    check = Check.check_manager.get(id=check_id)
    context = {"check": check}
    template = get_template('index.html')
    html = template.render(context)

    url = 'http://localhost:3000/'
    html_base64 = base64.b64encode(html.encode('utf-8')).decode('utf-8')
    data = {'contents': html_base64}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(data), headers=headers)

    pdf_temp = NamedTemporaryFile(delete=True)
    pdf_temp.write(response.content)
    pdf_temp.flush()

    check.status = "rendered"
    check.pdf_file.save(f"{check.order.get('order_id')}_{check.type}.pdf", File(pdf_temp))
    pdf_temp.close()
