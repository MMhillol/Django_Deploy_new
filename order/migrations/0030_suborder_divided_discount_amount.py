# Generated by Django 4.1.3 on 2023-05-14 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0029_suborder_delivery_charge'),
    ]

    operations = [
        migrations.AddField(
            model_name='suborder',
            name='divided_discount_amount',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
