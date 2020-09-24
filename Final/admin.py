from django.contrib import admin
from . import models

# Register your models here.


# An inline class for the resumes
class ResumeInformationInline(admin.TabularInline):

    model = models.Resume_Information
    list_display = ('owner', 'pdf_text', 'status')
    list_display_links = ('owner', 'pdf_text')
    search_fields = ['pdf_text']
    list_filter = ['status']
    extra = 0


class ResumeAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'file', 'date_pub')
    list_display_links = ('email', 'file')
    search_fields = ('email', 'name')
    list_filter = ['date_pub']
    inlines = [ResumeInformationInline]


admin.site.register(models.Resumes, ResumeAdmin)


class ResumeInformationAdmin(admin.ModelAdmin):
    list_display = ('owner', 'pdf_text', 'status')
    list_display_links = ('owner', 'pdf_text')
    search_fields = ['pdf_text']
    list_filter = ['status']


admin.site.register(models.Resume_Information, ResumeInformationAdmin)


