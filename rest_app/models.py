from django.db import models

# Create your models here.

class ProductsInfo(models.Model):
    id= models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    product_description = models.CharField(max_length=300)
    product_price = models.CharField(max_length=50)
    
    def __str__(self):
        return self.product_name