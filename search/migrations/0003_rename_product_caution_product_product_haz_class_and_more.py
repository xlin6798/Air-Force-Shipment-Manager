# Generated by Django 4.1.1 on 2022-10-17 02:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("search", "0002_alter_product_product_description"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="product_caution",
            new_name="product_haz_class",
        ),
        migrations.RenameField(
            model_name="product", old_name="product_class", new_name="product_pg",
        ),
        migrations.RenameField(
            model_name="product",
            old_name="product_description",
            new_name="product_psn",
        ),
        migrations.RenameField(
            model_name="product", old_name="product_group", new_name="product_sp",
        ),
        migrations.RenameField(
            model_name="product", old_name="product_name", new_name="product_sub_class",
        ),
        migrations.RemoveField(model_name="product", name="product_provisions",),
        migrations.RemoveField(model_name="product", name="product_warning",),
    ]
