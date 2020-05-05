from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class Resumes(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length = 100)
    file = models.FileField()
    date_pub = models.DateField('Date Uploaded')

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.date <= now

    was_published_recently.admin_order_field = 'date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def __str__(self):
        return self.email
