from django.db import models

# Create your models here.
class Product(models.Model):
    productname = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    image = models.CharField(max_length=5000, null=True, blank=True)

    def __str__(self) -> str:
        return self.productname

class ProductInventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.TimeField()
    modified_at = models.TimeField()
    deleted_at = models.TimeField()


