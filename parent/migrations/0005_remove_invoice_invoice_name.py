# Generated by Django 4.2.20 on 2025-03-19 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parent', '0004_invoice_invoice_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='invoice_name',
        ),
    ]
