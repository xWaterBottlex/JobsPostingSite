# Generated by Django 3.0.4 on 2020-03-31 09:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Job', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='created_on',
            field=models.DateTimeField(verbose_name=datetime.datetime(2020, 3, 31, 15, 12, 52, 746835)),
        ),
    ]
