# Generated by Django 4.2 on 2023-04-24 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("LC_SearchEngine", "0005_alter_leetcodedata_similar_questions"),
    ]

    operations = [
        migrations.AlterField(
            model_name="leetcodedata",
            name="acceptance_rate",
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name="leetcodedata",
            name="frequency",
            field=models.FloatField(),
        ),
    ]