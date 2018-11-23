import datetime

from django.db import models
from django.utils import timezone

# Create your models here.


class Organization(models.Model):
    def __str__(self):
        return self.org_name
    org_name = models.CharField(max_length=200)
    org_mission = models.CharField(max_length=10000, null=True)
    org_created = models.DateField('Date of Organization Creation')
    info_budget = models.BooleanField('Was an informational budget submitted?')

    def was_created_recently(self):
        return self.org_created >= timezone.now() - datetime.timedelta(days=1)


class InventoryItem(models.Model):
    def __str__(self):
        return self.item_name
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=200)
    purchase_date = models.DateField('Date of Purchase')
    delivery_date = models.DateField('Date of Delivery')
    item_value = models.DecimalField('Value of Item', max_digits=20, decimal_places=3)
    storage_location = models.CharField(max_length=1000)
    estimated_life = models.DurationField(help_text="This is entered in DD HH:MM:SS")


class Sanction(models.Model):
    def __str__(self):
        return self.sanction_type
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    application_date = models.DateField('Date of Sanction Application')
    sanction_duration = models.DurationField(help_text="This is entered in DD HH:MM:SS")
    sanction_type = models.CharField(max_length=1500)
    offense_description = models.CharField(max_length=10000)
