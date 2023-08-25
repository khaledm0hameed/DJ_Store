# Generated by Django 4.2 on 2023-08-08 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0039_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('shipped', 'Shipped'), ('delivered', 'Delivered'), ('cancelled', 'Cancelled')], default='pending', max_length=20, null=True),
        ),
    ]