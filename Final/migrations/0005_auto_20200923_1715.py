# Generated by Django 3.0.3 on 2020-09-23 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Final', '0004_auto_20200923_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume_information',
            name='rating',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='resume_information',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Final.Resumes'),
        ),
    ]
