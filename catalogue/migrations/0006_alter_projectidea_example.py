# Generated by Django 5.0 on 2023-12-17 14:42

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0005_alter_projectidea_effort_note_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectidea',
            name='example',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]