# Generated by Django 4.1.3 on 2022-12-19 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_alter_user_postcode_alter_user_village'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/user'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(blank=True, choices=[('FARMER', 'Farmer'), ('AGENT', 'Agent'), ('CUSTOMER', 'Customer')], max_length=50, null=True),
        ),
    ]
