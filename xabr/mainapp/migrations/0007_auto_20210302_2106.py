# Generated by Django 3.1.5 on 2021-03-02 18:06

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_auto_20210220_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='posts_text',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]