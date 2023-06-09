# Generated by Django 4.1.1 on 2022-12-01 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="HazClass",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("code", models.CharField(max_length=200)),
                ("desc", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="HazSubstance",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("psn", models.CharField(max_length=200)),
                ("weight_lbs", models.CharField(max_length=200)),
                ("weight_kgs", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("un", models.CharField(max_length=200)),
                ("psn", models.CharField(max_length=200)),
                ("hazard", models.CharField(max_length=200)),
                ("subrisk", models.CharField(max_length=200)),
                ("pg", models.CharField(max_length=200)),
                ("sp", models.CharField(max_length=200)),
                ("paragraph", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="SpCode",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("code", models.CharField(max_length=200)),
                ("desc", models.TextField()),
            ],
        ),
    ]
