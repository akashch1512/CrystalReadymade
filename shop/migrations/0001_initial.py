# Generated by Django 5.1.3 on 2024-11-29 16:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='shop/images')),
                ('original_price', models.DecimalField(decimal_places=2, default='', max_digits=10)),
                ('discounted_price', models.DecimalField(decimal_places=2, default='', max_digits=10)),
                ('description', models.TextField()),
                ('published_date', models.DateField()),
                ('category', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User_auth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='EightElementSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Section Name')),
                ('product1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='section_product1', to='shop.product')),
                ('product2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='section_product2', to='shop.product')),
                ('product3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='section_product3', to='shop.product')),
                ('product4', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='section_product4', to='shop.product')),
                ('product5', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='section_product5', to='shop.product')),
                ('product6', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='section_product6', to='shop.product')),
                ('product7', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='section_product7', to='shop.product')),
                ('product8', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='section_product8', to='shop.product')),
            ],
        ),
    ]
