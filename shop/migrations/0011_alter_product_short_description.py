# Generated by Django 5.1.3 on 2024-12-12 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_alter_product_tags_alter_product_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='short_description',
            field=models.CharField(blank=True, verbose_name='Short Description'),
        ),
    ]
