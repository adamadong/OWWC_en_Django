# Generated by Django 4.2.7 on 2023-11-07 13:32

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0008_team_place"),
    ]

    operations = [
        migrations.RenameField(
            model_name="team",
            old_name="place",
            new_name="lieu",
        ),
    ]
