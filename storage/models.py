from django.db import models

# Create your models here.
class Storage(models.Model):     
    product_name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.FileField(null=True, blank=True, upload_to='media/')
    
    class Meta:
        ordering = ['-id']
        
    def __str__(self):
        return f'{self.product_name}'