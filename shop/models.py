from django.db import models

# Create your models here
class search(models.Model):
    boot=models.CharField(max_length=200)
    def __str__(self):
        return self.boot

class Shoe(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    size = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField()

    def __str__(self):
        return self.name

