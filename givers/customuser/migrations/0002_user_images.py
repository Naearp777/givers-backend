# Generated by Django 3.2.4 on 2021-06-30 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='images',
            field=models.ImageField(default='avatar.jpg', upload_to='profile_Images'),
        ),
    ]