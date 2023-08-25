# Generated by Django 4.2 on 2023-07-21 04:30

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=60)),
                ('Price', models.FloatField()),
                ('Description', models.TextField(max_length=2000)),
                ('Image', models.ImageField(upload_to='images/')),
                ('Availability', models.BooleanField(default=True)),
                ('Color', colorfield.fields.ColorField(default='#FF0000', image_field=None, max_length=18, samples=None)),
                ('Categore', models.CharField(blank=True, choices=[('Laptop', 'Laptop'), ('Computer', 'Computer'), ('Phone', 'Phone'), ('Screen', 'Screen')], max_length=50, null=True)),
            ],
        ),
    ]
