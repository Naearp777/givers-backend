# Generated by Django 3.2.4 on 2021-07-13 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0003_auto_20210713_1630'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requestevents',
            name='interested',
        ),
    ]
