# Generated by Django 4.2 on 2023-09-16 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0068_product_have_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Color',
            field=models.CharField(blank=True, choices=[('Black', 'Black'), ('White', 'White'), ('Red', 'Red'), ('Green', 'Green'), ('Blue', 'Blue'), ('Yellow', 'Yellow'), ('Magenta', 'Magenta'), ('Cyan', 'Cyan'), ('Orange', 'Orange'), ('Purple', 'Purple')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='product_color',
            name='Color',
            field=models.CharField(blank=True, choices=[('Black', 'Black'), ('White', 'White'), ('Red', 'Red'), ('Green', 'Green'), ('Blue', 'Blue'), ('Yellow', 'Yellow'), ('Magenta', 'Magenta'), ('Cyan', 'Cyan'), ('Orange', 'Orange'), ('Purple', 'Purple')], max_length=30, null=True),
        ),
    ]