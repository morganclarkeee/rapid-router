# Generated by Django 3.2.16 on 2022-12-01 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    def add_next_level_to_last_levels(apps, schema_editor):
        Level = apps.get_model("game", "Level")
        db_alias = schema_editor.connection.alias
        Level_Object_Wrapper = Level.objects.using(db_alias)
        levels = Level_Object_Wrapper.filter(next_level=None).exclude(name="109")
        for level in levels:
            next_level_update = Level_Object_Wrapper.get(
                name=(str(int(level.name) + 1))
            )
            Level_Object_Wrapper.filter(name=level.name).update(
                next_level=next_level_update
            )

    def remove_next_level_to_last_levels(apps, schema_editor):
        Level = apps.get_model("game", "Level")
        db_alias = schema_editor.connection.alias
        Level_Object_Wrapper = Level.objects.using(db_alias)
        Level_Object_Wrapper.filter(
            name__in=["12", "18", "28", "32", "43", "50", "60", "67", "79", "91"]
        ).update(next_level=None)

    dependencies = [
        ("game", "0076_level_locked_for_class"),
    ]

    operations = [
        migrations.AlterField(
            model_name="level",
            name="next_level",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="prev_level",
                to="game.level",
            ),
        ),
        migrations.RunPython(
            add_next_level_to_last_levels, reverse_code=remove_next_level_to_last_levels
        ),
    ]