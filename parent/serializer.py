from django.db.models import fields
from rest_framework import serializers
from .models import Invoice
 
class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'