# Generated by Django 4.1.1 on 2022-09-16 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0015_alter_company_founded'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='founded',
        ),
    ]
