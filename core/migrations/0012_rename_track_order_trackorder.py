# Generated by Django 5.0.1 on 2024-05-10 15:25

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_track_order'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Track_Order',
            new_name='TrackOrder',
        ),
    ]