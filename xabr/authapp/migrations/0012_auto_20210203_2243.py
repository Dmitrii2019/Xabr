# Generated by Django 3.1 on 2021-02-03 19:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0011_auto_20210203_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='xabruser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 5, 19, 43, 55, 608867, tzinfo=utc)),
        ),
    ]
