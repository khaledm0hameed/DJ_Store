# Generated by Django 4.2 on 2023-07-31 03:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0021_rename_image_category_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='availability',
            new_name='Availability',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='brand',
            new_name='Brand',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='color',
            new_name='Color',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='Image',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='Price',
        ),
    ]
