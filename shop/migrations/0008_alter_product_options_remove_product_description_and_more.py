# Generated by Django 5.1.3 on 2024-12-11 14:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_alter_profile_user_profile_photo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_name',
        ),
        migrations.AddField(
            model_name='product',
            name='additional_images',
            field=models.JSONField(blank=True, help_text='Store additional image URLs as a JSON array', null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(blank=True, max_length=100, verbose_name='Brand'),
        ),
        migrations.AddField(
            model_name='product',
            name='detailed_description',
            field=models.TextField(blank=True, verbose_name='Detailed Description'),
        ),
        migrations.AddField(
            model_name='product',
            name='dimensions',
            field=models.CharField(blank=True, help_text='Product dimensions (e.g., LxWxH)', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='is_available',
            field=models.BooleanField(default=True, verbose_name='Is Available'),
        ),
        migrations.AddField(
            model_name='product',
            name='main_image',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='meta_description',
            field=models.TextField(blank=True, help_text='Meta description for SEO'),
        ),
        migrations.AddField(
            model_name='product',
            name='meta_title',
            field=models.CharField(blank=True, help_text='Meta title for SEO', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Product Name'),
        ),
        migrations.AddField(
            model_name='product',
            name='short_description',
            field=models.CharField(blank=True, max_length=255, verbose_name='Short Description'),
        ),
        migrations.AddField(
            model_name='product',
            name='sku',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='SKU'),
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, help_text='Unique identifier for the product URL', null=True, unique=True),
        ),
        migrations.AddField(
            model_name='product',
            name='stock_quantity',
            field=models.PositiveIntegerField(default=0, verbose_name='Stock Quantity'),
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.CharField(blank=True, help_text='Comma-separated tags for the product', max_length=255),
        ),
        migrations.AddField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Last Updated'),
        ),
        migrations.AddField(
            model_name='product',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Weight (kg)'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(max_length=50, verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='discounted_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Discounted Price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='original_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Original Price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='published_date',
            field=models.DateField(auto_now_add=True, verbose_name='Published Date'),
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(blank=True, null=True)),
                ('alt_text', models.CharField(blank=True, max_length=255, verbose_name='Alt Text')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='shop.product')),
            ],
            options={
                'verbose_name': 'Product Image',
                'verbose_name_plural': 'Product Images',
            },
        ),
    ]
