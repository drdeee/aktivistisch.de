# Generated by Django 5.0 on 2024-01-13 12:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0021_projectidea_draft'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectidea',
            name='effort_note',
        ),
        migrations.RemoveField(
            model_name='projectidea',
            name='experience_note',
        ),
        migrations.AlterField(
            model_name='projectidea',
            name='experience_level',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
    ]
