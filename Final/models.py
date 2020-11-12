from django.db import models
import datetime
from django.utils import timezone
from django.contrib.postgres.fields import JSONField

# Create your models here.

#
class Job(models.Model):
    name=models.CharField(max_length=40)
    role=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Resumes(models.Model):
    name = models.CharField(max_length=100, verbose_name="Full Name")
    email = models.EmailField(max_length = 100, unique = True, verbose_name="Email")
    file = models.FileField(upload_to='resume', verbose_name="Resume")
    position = models.ForeignKey(Job, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Applying Position")
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



class Job_Requirement(models.Model):
    job=models.ForeignKey(Job, on_delete=models.CASCADE)
    requirement=models.TextField()

    def __str__(self):
        return self.requirement

class Job_Keyword(models.Model):
    job=models.ForeignKey(Job, on_delete=models.CASCADE)
    keyword=models.CharField(max_length=30)

    def __str__(self):
        return self.keyword
