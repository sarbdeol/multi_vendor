# Generated by Django 3.2.12 on 2022-02-08 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_alter_product_product_vendor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='PRDCost',
            field=models.FloatField(blank=True, null=True, verbose_name='Cost'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PRDDiscountPrice',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Discount'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PRDPrice',
            field=models.FloatField(blank=True, null=True, verbose_name='Price'),
        ),
    ]
