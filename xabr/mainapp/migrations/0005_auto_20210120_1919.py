# Generated by Django 3.1.5 on 2021-01-20 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20210120_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(default='new', max_length=64, unique=True, verbose_name='название категории'),
        ),
    ]