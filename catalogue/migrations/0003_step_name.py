# Generated by Django 5.0 on 2023-12-16 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0002_alter_projectidea_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='step',
            name='name',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
    ]