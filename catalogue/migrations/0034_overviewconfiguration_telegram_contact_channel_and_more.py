# Generated by Django 5.0 on 2024-03-20 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0033_alter_party_options_party_border'),
    ]

    operations = [
        migrations.AddField(
            model_name='overviewconfiguration',
            name='telegram_contact_channel',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='overviewconfiguration',
            name='telegram_token',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
