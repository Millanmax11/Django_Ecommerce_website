# Generated by Django 5.0.1 on 2024-03-24 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_rename_shipping_address_address_town_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='reference_code',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
