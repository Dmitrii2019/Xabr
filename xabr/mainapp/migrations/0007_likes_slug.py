# Generated by Django 3.1 on 2021-02-02 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_remove_likes_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='likes',
            name='slug',
            field=models.SlugField(default='', max_length=70, verbose_name='URL'),
        ),
    ]