# Generated by Django 4.1.3 on 2023-06-05 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_offer_offerproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='commission',
            field=models.FloatField(default=0, help_text='Agent Commission', max_length=255),
        ),
    ]
