# Generated by Django 4.2 on 2023-05-05 07:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('FEST', '0003_alter_event_block'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='Date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Date'),
            preserve_default=False,
        ),
    ]
