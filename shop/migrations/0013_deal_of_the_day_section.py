# Generated by Django 5.1.3 on 2024-12-13 05:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_remove_product_slug_sectionelement_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deal_of_the_day_section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Section Name deal')),
                ('Days', models.PositiveIntegerField(default=0, verbose_name='Days')),
                ('Hours', models.PositiveIntegerField(default=0, verbose_name='Days')),
                ('min', models.PositiveIntegerField(default=0, verbose_name='Days')),
                ('sec', models.PositiveIntegerField(default=0, verbose_name='Days')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='section_product_product', to='shop.product')),
            ],
        ),
    ]