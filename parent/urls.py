from django.urls import path
from parent import views

urlpatterns = [
    path("invoice_post", views.InvoiceCreateView.as_view(), name="invoice_create"),
    path("invoice_list", views.InvoiceListView.as_view(), name="invoice_list")
]