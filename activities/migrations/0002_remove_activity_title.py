# Generated by Django 4.1.1 on 2022-09-11 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='title',
        ),
    ]
