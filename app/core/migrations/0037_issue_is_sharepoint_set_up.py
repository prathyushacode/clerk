# Generated by Django 3.2.6 on 2021-09-25 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0036_alter_issuenote_note_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="issue",
            name="is_sharepoint_set_up",
            field=models.BooleanField(default=False),
        ),
    ]