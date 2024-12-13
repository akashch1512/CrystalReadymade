# Generated by Django 5.1.3 on 2024-12-13 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_deal_of_the_day_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal_of_the_day_section',
            name='Hours',
            field=models.PositiveIntegerField(default=0, verbose_name='Hours'),
        ),
        migrations.AlterField(
            model_name='deal_of_the_day_section',
            name='min',
            field=models.PositiveIntegerField(default=0, verbose_name='Min'),
        ),
        migrations.AlterField(
            model_name='deal_of_the_day_section',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Dont_Change_this'),
        ),
        migrations.AlterField(
            model_name='deal_of_the_day_section',
            name='sec',
            field=models.PositiveIntegerField(default=0, verbose_name='Sec'),
        ),
    ]
