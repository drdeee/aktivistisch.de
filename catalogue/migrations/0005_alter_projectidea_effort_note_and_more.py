# Generated by Django 5.0 on 2023-12-16 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0004_alter_projectidea_effort_note_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectidea',
            name='effort_note',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='projectidea',
            name='experience_note',
            field=models.TextField(max_length=100, null=True),
        ),
    ]
