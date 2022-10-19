from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
<<<<<<< HEAD
    image = models.ImageField(null=True, blank=True, upload_to='media/')
=======
    image = models.ImageField(null=True, blank=True, upload_to='images/')
>>>>>>> main

    def __str__(self):
        return f'{self.product_name}'

class ProductInventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.TimeField()
    modified_at = models.TimeField()
    deleted_at = models.TimeField()

    def __str__(self):
        return f'{self.product} {self.quantity}'


