from django.db import models

# Create your models here.
class DressCategory(models.Model):
    id=models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.category_name
    
class DressDetails(models.Model):
    id = models.AutoField(primary_key=True)
    dress_name = models.CharField(max_length=100)
    dress_price = models.CharField(max_length=50)
    dress_image = models.URLField(max_length=5000)
    dress_category = models.ForeignKey(DressCategory,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.dress_name