from django.db.models import fields
from django.forms import ModelForm
from .models import Mall, Grocery

class MallForm(ModelForm):
    class Meta:
        model = Mall
        fields = '__all__'


class GroceryForm(ModelForm):
    class Meta:
        model = Grocery
        fields = '__all__'