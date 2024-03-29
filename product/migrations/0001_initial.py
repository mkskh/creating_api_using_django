# Generated by Django 5.0.3 on 2024-03-07 14:42

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
                ('product_name', models.CharField(max_length=200)),
                ('product_category', models.CharField(choices=[('ELECTRONICS', 'Electronics'), ('BOOKS', 'Books'), ('CLOTHING', 'Clothing'), ('FOOD', 'Food'), ('HOME_APPLIANCES', 'Home Appliances'), ('BEAUTY', 'Beauty'), ('TOYS', 'Toys'), ('SPORTS', 'Sports'), ('FURNITURE', 'Furniture'), ('JEWELRY', 'Jewelry'), ('OTHER', 'Other')], max_length=20)),
                ('product_description', models.TextField()),
                ('product_image_url', models.CharField(max_length=1000)),
                ('product_price', models.FloatField()),
            ],
        ),
    ]
