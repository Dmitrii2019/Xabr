# Generated by Django 2.2 on 2021-02-25 13:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0008_auto_20210220_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='xabruser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 27, 13, 35, 27, 270579, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='xabruser',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='first name'),
        ),
    ]
