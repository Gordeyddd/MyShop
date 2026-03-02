from django.db import models
from tkinter.constants import CASCADE

class Category(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name




class Product (models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='images/')
    descripion = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    slug = models.CharField(unique=True, max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product')
    def __str__(self):
        return self.name



