from django.db import models


class Product(models.Model):
    CATEGORY_CHOICES = [
        ('ELECTRONICS', 'Electronics'),
        ('BOOKS', 'Books'),
        ('CLOTHING', 'Clothing'),
        ('FOOD', 'Food'),
        ('HOME_APPLIANCES', 'Home Appliances'),
        ('BEAUTY', 'Beauty'),
        ('TOYS', 'Toys'),
        ('SPORTS', 'Sports'),
        ('FURNITURE', 'Furniture'),
        ('JEWELRY', 'Jewelry'),
        ('OTHER', 'Other'),
    ]
    product_name = models.CharField(max_length=200)
    product_category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    product_description = models.TextField()
    product_image_url = models.CharField(max_length=1000)
    product_price = models.FloatField()

    def __str__(self):
        return self.product_name
