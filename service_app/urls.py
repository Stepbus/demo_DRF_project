from django.urls import path

from service_app import views

urlpatterns = [
    path("new-order", views.new_order, name='new-order'),
    path("printer/<str:api_key>", views.printer_checker, name='printer'),
]
