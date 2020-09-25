from django.db import models
import datetime
from django.utils import timezone
from django.contrib.postgres.fields import JSONField

# Create your models here.


class Resumes(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length = 100, unique = True)
    file = models.FileField(upload_to='resume')
    date_pub = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = "Resumes"
        verbose_name = "Resume"

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.date_pub <= now

    was_published_recently.admin_order_field = 'date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def __str__(self):
        return self.email


class Resume_Information(models.Model):
    owner = models.OneToOneField(Resumes, on_delete=models.CASCADE)
    pdf_text = models.TextField()
    status = models.BooleanField(default=False)
    rating=models.FloatField()
    date_pub = models.DateTimeField(default=timezone.now)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.date_pub <= now

    was_published_recently.admin_order_field = 'date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    # returning the name of the resume owner
    # def name(self):
    #     resume = Resumes.objects.filter(id=self.owner).get()
    #     return resume.email
    #
    # name.short_description = "Resume Owner"

    def __str__(self):
        return self.owner.name

    class Meta:
        verbose_name_plural = "Uploaded Resumes"
        verbose_name = "Uploaded Resume"

#
# class Resume_Information_Pictures(models.Model):
#     info = models.ForeignKey(Resumes, on_delete=models.CASCADE)
#     picture = models.ImageField(upload_to = 'resume_pics')
