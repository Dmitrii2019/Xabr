# Generated by Django 3.1 on 2021-02-05 21:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0035_auto_20210206_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='xabruser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 7, 21, 14, 12, 233903, tzinfo=utc)),
        ),
    ]
