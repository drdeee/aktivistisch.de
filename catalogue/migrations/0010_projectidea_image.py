# Generated by Django 5.0 on 2023-12-22 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0009_rename_idea_step_project_idea'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectidea',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
