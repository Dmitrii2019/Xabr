# Generated by Django 3.1.5 on 2021-01-28 18:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_auto_20210127_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='xabruser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 30, 18, 35, 12, 35524, tzinfo=utc)),
        ),
    ]