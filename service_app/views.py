import json

from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

from service_app.models import Check, Printer
from service_app.tasks import create_pdf

"""
I used csrf_exempt only for the test - because I use Postman to get the json data for validation.
In a real project, I think this data should come from a Django form or via a json from frontend
"""


@csrf_exempt
def new_order(request):
    """
    order should be as follows:
        {
        "order":
            {
                "order_id": 9999,
                "product":
                    [
                    {"product1": "product1",
                    "product2": "product2"}
                    ]
            },
        "point_id": 1234
        }
    """
    if request.method == 'POST':
        try:
            order = json.loads(request.body.decode('utf-8'))
        except json.JSONDecodeError:
            return JsonResponse({"status": "Failed", "error": "Invalid JSON"}, status=400)
        except Exception as e:
            return JsonResponse({"status": "Failed", "error": str(e)}, status=500)

        printers = Printer.printer_manager.filter(point_id=order.get("point_id"))
        if not printers:
            return JsonResponse({"status": "Info", "message": f'No printers at point {order.get("point_id")}'})
        order_exists = Check.check_manager.filter(order=order.get("order")).first()
        if order_exists:
            return JsonResponse(
                {"status": "Info", "message": f'Order # {order_exists.order.get("order_id")} already exists'})

        for printer in printers:
            new_check = Check.check_manager.create(
                printer=printer,
                type=printer.check_type,
                order=order.get("order"),
                status="new",
            )
            create_pdf.delay(new_check.id)
        return JsonResponse({"status": "Success!", **order}, status=201)

    else:
        return HttpResponseBadRequest("Only POST method is allowed")


def printer_checker(request, api_key):
    printer = Printer.printer_manager.get(api_key=api_key)
    if not printer:
        return JsonResponse({"status": "Failed", "error": f"No printer found with the given ID {api_key}."}, status=404)
    checks_to_print = Check.check_manager.filter(printer=printer, status='rendered')
    if not checks_to_print:
        return JsonResponse({"status": "Info", "message": "No checks to print for this printer."})
    for check in checks_to_print:
        pdf_path = check.pdf_file.path
        check.status = 'printed'
        check.save()
    return JsonResponse({"status": "Success!", "message": f"{len(checks_to_print)} checks printed."})
