from rest_framework import generics

from parent.serializer import InvoiceSerializer
from parent.models import Invoice
# Create your views here.

class InvoiceCreateView(generics.CreateAPIView):
    serializer_class = InvoiceSerializer

class InvoiceListView(generics.ListAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer