from django.db import models


class InvoiceStatus(models.Model):
    name = models.CharField("status Name", max_length=10)

    class Meta:
        verbose_name = "Status"


class Invoice(models.Model):
    number = models.CharField("Invoice Number", max_length=64)
    oay_amount = models.IntegerField()
    status = models.ForeignKey(InvoiceStatus, verbose_name="Status Name", on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Invoice"