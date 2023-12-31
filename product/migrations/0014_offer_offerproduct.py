# Generated by Django 4.1.3 on 2023-05-25 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_product_created_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(default='', help_text='name', max_length=100)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('thumbnail', models.FileField(blank=True, null=True, upload_to='offers')),
                ('short_description', models.CharField(blank=True, default='', max_length=800, null=True)),
                ('full_description', models.TextField(blank=True, default='', null=True)),
                ('discount_price', models.FloatField(blank=True, default=0, max_length=255, null=True)),
                ('discount_price_type', models.CharField(choices=[('per', 'Percentage'), ('flat', 'Flat')], default='per', max_length=20)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Offer',
                'verbose_name_plural': 'Offers',
                'db_table': 'offer',
            },
        ),
        migrations.CreateModel(
            name='OfferProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('offer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='offer_product_offer', to='product.offer')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='offer_offer_product', to='product.product')),
            ],
            options={
                'verbose_name': 'OfferProduct',
                'verbose_name_plural': 'OfferProducts',
                'db_table': 'offer_products',
            },
        ),
    ]
