from django.db import models

# Create your models here.
class InvoiceExtended(models.Model):
    extends = "Invoice"

    invoice_name = models.CharField("Name", max_length=64, null=True)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        abstract = True