# Generated by Django 4.1.3 on 2023-02-28 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0010_rename_suborder_id_suborder_suborder_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='suborder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_item_suborder', to='order.suborder'),
        ),
    ]
