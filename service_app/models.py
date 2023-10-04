from django.db import models


CHECK_TYPE_CHOICES = [
    ('kitchen', 'Kitchen'),
    ('client', 'Client'),
]

STATUS_CHOICES = [
    ('new', 'New'),
    ('rendered', 'Rendered'),
    ('printed', 'Printed'),
]


class Printer(models.Model):
    printer_manager = models.Manager()

    name = models.CharField(max_length=255)
    api_key = models.CharField(max_length=255, unique=True)
    check_type = models.CharField(max_length=50, choices=CHECK_TYPE_CHOICES)
    point_id = models.IntegerField()

    def __str__(self):
        return self.name


class Check(models.Model):
    check_manager = models.Manager()

    printer = models.ForeignKey(Printer, on_delete=models.CASCADE)
    type = models.CharField(max_length=50, choices=CHECK_TYPE_CHOICES)
    order = models.JSONField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    pdf_file = models.FileField(upload_to='pdf/', blank=True)

    def __str__(self):
        return f"Check for: {self.printer.name}"
