# Django Models Inheritance

## Installing pipeline
```bash
pip3 install -r requirements.txt

python3 manage.py makemigration

python3 manage.py migrate

python3 manage.py runserver
```

## How it works
This pipeline dynamically extends Django models across apps by injecting fields and methods from child models into parent models at runtime. During startup, ready() in child.apps triggers extend_models(), which scans child.models for abstract models with an extends attribute. It then finds the corresponding parent models and merges additional fields and methods into them before Django finalizes the ORM. No extra database tables are created, and all extended functionality is seamlessly available in the base model, enabling flexible multi-client customizations without modifying core models.

## Exaple for using

### In this repo there are 2 applicaions: 
- parent (base application for all cliens)
- child (optional application dedicated to the client for inheritance models specified in parent class)

### Implemented parent model [**parent/models.py**]
```python
class Invoice(models.Model):
    number = models.CharField("Invoice Number", max_length=64)
    pay_amount = models.IntegerField()
    status = models.ForeignKey(InvoiceStatus, verbose_name="Status Name", on_delete=models.SET_NULL, null=True)
```
### Implemented child model [**child/models.py**]
```python
class InvoiceExtended(models.Model):
    extends = "Invoice" # Mandatory to specify model from @parent

    invoice_name = models.CharField("Name", max_length=64, null=True)
    
    class Meta:
        # Set abstract = True if you want inherit existing model from base OR don`t specify if you want to create new table in db for model
        abstract = True
```

### Overload methid in [**child/apps.py**]
```python
class ChildConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'child'

    def ready(self):
        from core.patcher import extend_models
        extend_models(self.name)
```

And here we are, you can test inheritance by dis/including **child** app in **core/settings.py**

### Try this endoinds for testing Create/Get Invoices

- /api/invoice_post
- /api/invoice_list
