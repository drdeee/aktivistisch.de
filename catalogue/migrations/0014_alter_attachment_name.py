# Generated by Django 5.0 on 2023-12-23 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0013_alter_projectidea_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
