# Generated by Django 5.0.1 on 2024-05-15 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_trackorder_courier_approved_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='trackorder',
            name='confirmed_approved',
            field=models.BooleanField(default=False),
        ),
    ]
