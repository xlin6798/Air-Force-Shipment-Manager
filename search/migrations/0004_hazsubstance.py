# Generated by Django 4.1.1 on 2022-11-20 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("search", "0003_alter_hazclass_desc_alter_spcode_desc"),
    ]

    operations = [
        migrations.CreateModel(
            name='HazSubstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('haz_psn', models.CharField(max_length=200)),
                ('haz_weight_pounds', models.CharField(max_length=200)),
                ('haz_weight_kilograms', models.CharField(max_length=200)),
            ],
        ),
    ]
