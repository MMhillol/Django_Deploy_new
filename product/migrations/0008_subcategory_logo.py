# Generated by Django 4.1.3 on 2022-12-11 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_category_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='sub_category'),
        ),
    ]
