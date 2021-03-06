# Generated by Django 3.2.5 on 2021-08-13 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0022_auto_20210812_1742'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='country',
        ),
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='district',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='municipality',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='province',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='ward',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
