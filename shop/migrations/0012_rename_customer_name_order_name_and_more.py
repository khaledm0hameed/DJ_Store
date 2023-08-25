# Generated by Django 4.2 on 2023-07-28 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_remove_cartitem_order_alter_cartitem_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='customer_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='Phone',
            new_name='phone',
        ),
        migrations.RemoveField(
            model_name='order',
            name='created_at',
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(default=17, on_delete=django.db.models.deletion.CASCADE, to='shop.product'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.TextField(),
        ),
    ]
