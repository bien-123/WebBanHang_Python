# Generated by Django 3.2.15 on 2023-08-20 10:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='time_create',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 20, 10, 54, 41, 607141, tzinfo=utc)),
        ),
    ]
