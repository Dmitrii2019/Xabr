# Generated by Django 3.1 on 2021-02-02 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20210201_2321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='like',
            name='user',
        ),
        migrations.DeleteModel(
            name='Tweet',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]