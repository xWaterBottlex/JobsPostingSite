# Generated by Django 3.0.4 on 2020-03-31 09:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Job', '0002_auto_20200331_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 31, 9, 48, 7, 307327, tzinfo=utc)),
        ),
    ]
