# Generated by Django 5.0.6 on 2024-07-05 00:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dormmatch", "0003_rename_num_occupied_dorminfo_capacity"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dorminfo",
            name="dorm_class",
            field=models.CharField(choices=[("A", "A"), ("B", "B")], max_length=1),
        ),
    ]
