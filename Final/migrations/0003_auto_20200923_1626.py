# Generated by Django 3.0.3 on 2020-09-23 13:26

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Final', '0002_auto_20200724_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume_information',
            name='pdf_text',
            field=django.contrib.postgres.fields.jsonb.JSONField(),
        ),
        migrations.DeleteModel(
            name='Resume_Information_Pictures',
        ),
    ]
