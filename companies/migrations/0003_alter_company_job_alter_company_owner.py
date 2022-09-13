# Generated by Django 4.1.1 on 2022-09-13 12:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_job_company_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('companies', '0002_company_job_alter_company_company_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='job',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='company', to='jobs.job'),
        ),
        migrations.AlterField(
            model_name='company',
            name='owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='companies', to=settings.AUTH_USER_MODEL),
        ),
    ]
