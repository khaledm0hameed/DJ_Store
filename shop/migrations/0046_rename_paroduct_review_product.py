# Generated by Django 4.2 on 2023-08-08 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0045_review_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='paroduct',
            new_name='product',
        ),
    ]