# Generated by Django 4.1.1 on 2022-09-09 11:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(default=None, max_length=200)),
                ('post_date', models.DateField(default=None)),
                ('location', models.CharField(default=None, max_length=250)),
                ('salary', models.CharField(default=None, max_length=50)),
                ('benefits', models.TextField(default=None, max_length=500)),
                ('job_url', models.URLField(default=None)),
                ('requirements', models.TextField(default=None, max_length=500)),
                ('description', models.TextField(default=None, max_length=500)),
                ('job_status', models.CharField(choices=[('Saved', 'Saved'), ('Applied', 'Applied'), ('Interview', 'Interview'), ('Offer', 'Offer'), ('Declined', 'Not Interested')], default='Saved', max_length=100)),
                ('job_type', models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time'), ('Temporary', 'Temporary'), ('Contract', 'Contract'), ('Internship', 'Internship')], default=None, max_length=100)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
