# Generated by Django 3.0.3 on 2020-09-24 14:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Final', '0006_auto_20200923_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume_information',
            name='date_pub',
            field=models.DateField(default=datetime.datetime(2020, 9, 24, 14, 14, 51, 720192, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='resumes',
            name='date_pub',
            field=models.DateField(default=datetime.datetime(2020, 9, 24, 14, 14, 51, 679577, tzinfo=utc)),
        ),
    ]
