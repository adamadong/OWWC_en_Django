# Generated by Django 4.2.7 on 2023-11-07 13:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0004_rename_nb_player_team_rank"),
    ]

    operations = [
        migrations.AlterField(
            model_name="team",
            name="rank",
            field=models.IntegerField(),
        ),
    ]