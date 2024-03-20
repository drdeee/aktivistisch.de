# Generated by Django 5.0 on 2024-03-20 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0034_overviewconfiguration_telegram_contact_channel_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactFormEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('contact', models.EmailField(blank=True, max_length=100, null=True)),
                ('message', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='overviewconfiguration',
            name='email',
            field=models.EmailField(default='mail@aktivistisch.de', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='overviewconfiguration',
            name='pgp_key_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
