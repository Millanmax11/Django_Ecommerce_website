# Generated by Django 5.0.1 on 2024-03-24 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_rename_town_address_checkout_checkouts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkout',
            old_name='Checkouts',
            new_name='town_address',
        ),
    ]
