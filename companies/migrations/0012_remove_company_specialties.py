# Generated by Django 4.1.1 on 2022-09-14 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0011_company_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='specialties',
        ),
    ]
