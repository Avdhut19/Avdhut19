# Generated by Django 5.1.2 on 2024-11-11 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shravan', '0002_remove_invoice_state_alter_invoice_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoice',
            old_name='invoice_date',
            new_name='Invoice_date',
        ),
    ]