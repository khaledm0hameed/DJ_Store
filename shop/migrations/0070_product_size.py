# Generated by Django 4.2 on 2023-09-16 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0069_alter_product_color_alter_product_color_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Size', models.CharField(blank=True, choices=[('s', 's'), ('m', 'm'), ('l', 'l'), ('xl', 'xl')], max_length=30, null=True)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Product_Size', to='shop.product')),
            ],
        ),
    ]