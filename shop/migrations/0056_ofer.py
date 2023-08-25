# Generated by Django 4.2 on 2023-08-17 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0055_category_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ofer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='ofer/')),
                ('price', models.IntegerField()),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ofer_product', to='shop.product')),
            ],
        ),
    ]