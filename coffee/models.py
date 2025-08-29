from django.db import models

from django.db import models

# Coffee model
class Coffee(models.Model):
    CATEGORY_CHOICES = [
        ('hot', 'Hot Coffee'),
        ('cold', 'Cold Coffee'),
        ('special', 'Special Coffee'),
    ]

    name = models.CharField(max_length=255)
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.ImageField(upload_to="coffee/")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='hot')

    def __str__(self):
        return self.name


# CartItem model
class CartItem(models.Model):
    product = models.ForeignKey(Coffee, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"
    
    def get_total(self):
        return self.product.price * self.quantity

    
    
