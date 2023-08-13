# Generated by Django 4.1.3 on 2023-03-06 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0021_merge_20230305_1014'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[('DUE', 'Due'), ('PAID', 'Paid')], default='DUE', max_length=4)),
                ('date', models.DateField(auto_now_add=True)),
                ('farmer_account_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='order.farmeraccountinfo')),
                ('order_items', models.ManyToManyField(related_name='payments', to='order.orderitem')),
            ],
            options={
                'verbose_name': 'Payment_history',
                'verbose_name_plural': 'Payments_history',
                'db_table': 'payments_history',
            },
        ),
    ]
