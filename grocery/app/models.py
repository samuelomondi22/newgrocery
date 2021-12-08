
# Create your models here.
from django.contrib import admin
from django.db import models
from django.urls import reverse

# Create your models here.
MALL = (
    ('WALMART', 'Walmart'),
    ('BROULIM', 'Broulim'),
    ('ALBERTSON', 'Albertson')
)

class Grocery(models.Model):
    item_name = models.CharField(max_length=30)

    # Returns the item name in the terminal
    def __str__(self):
        return self.item_name

    # Gives you the details of searched 
    def get_absolute_url(self):
        return reverse('detail', kwargs={'grocery_id': self.id})


class Mall(models.Model):
    # date = models.DateField('date-item-entered')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    item_mall = models.CharField(max_length=20, choices=MALL, default='WALMART')

    # Comes from the Grocery table
    grocery = models.ForeignKey(Grocery, on_delete=models.CASCADE)

    # Allows you to order by item price
    class Meta:
        ordering = ['item_price']

class OrderItem(models.Model):
    item = models.ForeignKey(Grocery, on_delete=models.CASCADE)