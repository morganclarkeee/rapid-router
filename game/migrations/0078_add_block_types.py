# Generated by Django 3.2.16 on 2022-12-02 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0077_alter_level_next_level'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='block',
            options={'ordering': ['block_type', 'pk']},
        ),
        migrations.AddField(
            model_name='block',
            name='block_type',
            field=models.IntegerField(choices=[(0, 'Start'), (1, 'Action'), (2, 'Condition'), (3, 'Procedure'), (4, 'ControlFlow')], default=4),
            preserve_default=False,
        ),
    ]