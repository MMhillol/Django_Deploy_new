# Generated by Django 4.1.3 on 2022-11-27 05:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price_par_unit',
            new_name='price_per_unit',
        ),
    ]
