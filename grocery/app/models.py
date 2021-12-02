
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

    def __str__(self):
        return self.item_name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'grocery_id': self.id})


class Mall(models.Model):
    # date = models.DateField('date-item-entered')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    item_mall = models.CharField(max_length=20, choices=MALL, default='WALMART')
    grocery = models.ForeignKey(Grocery, on_delete=models.CASCADE)
    class Meta:
        ordering = ['item_price']
