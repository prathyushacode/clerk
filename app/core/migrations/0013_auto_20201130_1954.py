# Generated by Django 3.1.3 on 2020-11-30 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20201128_1717'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='is_eligible',
        ),
        migrations.RemoveField(
            model_name='person',
            name='company',
        ),
        migrations.AddField(
            model_name='client',
            name='can_speak_non_english',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='client',
            name='gender',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='gender_details',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='is_aboriginal_or_torres_strait_islander',
            field=models.BooleanField(default=False),
        ),
    ]
