# Generated by Django 4.1.5 on 2023-01-19 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pphoto',
            name='media',
            field=models.CharField(default='', max_length=100),
        ),
    ]
