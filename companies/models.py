from django.db import models

# Create your models here.

class Company(models.Model):
  owner = models.ForeignKey(
  'jwt_auth.User',
  related_name="companies",
  on_delete= models.CASCADE
)
  name = models.CharField(max_length=200, default=None)
  industry = models.CharField(max_length=200, default=None, blank=True)
  founded = models.IntegerField(blank=True)
  hq_location = models.CharField(max_length=200, default=None, blank=True)
  size = models.CharField(max_length=200, default=None, blank=True)
  type = models.CharField(max_length=200, default=None, blank=True)
  specialties = models.TextField(max_length=500, default=None, blank=True)
  company_url = models.URLField(max_length=200, default=None, blank=True)
  description = models.TextField(max_length=500, default=None, blank=True)