# Generated by Django 4.2.7 on 2023-11-07 13:06

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_equipment_pic_url_team_flag_url"),
    ]

    operations = [
        migrations.RenameField(
            model_name="team",
            old_name="rank",
            new_name="state",
        ),
    ]