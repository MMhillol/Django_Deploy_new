# Generated by Django 4.1.3 on 2022-11-27 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_remove_productionstep_title_productionstep_step'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='full_description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=800),
        ),
    ]