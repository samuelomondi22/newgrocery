
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
    item_comment = models.TextField(max_length=250)
    item_rate = models.IntegerField()

    def __str__(self):
        return self.item_name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'grocery_id': self.id})


class Mall(models.Model):
    date = models.DateField('date-item-entered')
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    item_mall = models.CharField(
        max_length=20, choices=MALL, default='WALMART')
    grocery = models.ForeignKey(Grocery, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_item_mall_display()} on {self.date}"
