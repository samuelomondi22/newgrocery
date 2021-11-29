from django import template
from django.db.models.query import InstanceCheckMeta
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import Grocery, Mall
from django.db.models import Q, fields
from django.forms import ModelForm
from .forms import MallForm, GroceryForm
import datetime as dt
from django.template import RequestContext
from django.http import HttpResponse, request
from django.core.exceptions import ValidationError
from django.contrib import messages

# Create your views here.


class HomePageView(TemplateView):
    template_name = 'home.html'

class GroceryDetail(TemplateView):
    template_name = 'detail.html'
    
class SearchGrocery(TemplateView):
    template_name = 'add_grocery.html'

    # retrieve and check if the item_name exist if it does call the add mall function is not then this function below is called
    def post(self, request):
        if self.request.method == 'POST':
            if self.request.POST.get('item_name') and self.request.POST.get('item_comment') and self.request.POST.get('item_rate') and self.request.POST.get('date') and self.request.POST.get(
                    'item_price') and self.request.POST.get('item_mall'):
                item_name = self.request.POST.get('item_name')
                item_comment = self.request.POST.get('item_comment')
                item_rate = self.request.POST.get('item_rate')
                grocery = Grocery(
                    item_name=item_name, item_comment=item_comment, item_rate=item_rate)
                grocery.save()
                date = self.request.POST.get('date')
                item_price = self.request.POST.get('item_price')
                item_mall = self.request.POST.get('item_mall')  
                grocery.mall_set.create(date=date, item_price=item_price, item_mall=item_mall, grocery=grocery)
                grocery.save()
                messages.success(self.request, "Item Added Successfully")

                return render(self.request, './templates/add_grocery.html', {})

            else:
                return render(self.request, '../templates/add_grocery.html', {})


class NoGrocery(TemplateView):
    template_name = 'modalsection.html'

class SearchResultsView(ListView):
    template_name = 'search_results.html'
    # have this give a pop up message if the item searched for isn't there and give an option of continue to search or add
    # the item
    def get_queryset(self): 
        query = self.request.GET.get('q')
        if Grocery.objects.filter(item_name=query).exists():
            object_list = Grocery.objects.get(
            Q(item_name__icontains=query))
            return object_list
        else:
            messages.error(self.request,"Item does not exist in the database would you like to add?")
            return redirect("search_results.html")
    
    def post(self, request):
        grocery = self.get_queryset()
        if self.request.method == 'POST':
            if self.request.POST.get('date') and self.request.POST.get('item_price') and self.request.POST.get('item_mall'):
                date = self.request.POST.get('date')
                item_price = self.request.POST.get('item_price')
                item_mall = self.request.POST.get('item_mall')
                mall = Mall(date=date, item_price=item_price, item_mall=item_mall, grocery=grocery)
                mall.save()
                messages.success(self.request, "Mall Added Successfully")

                return render(self.request, './templates/search_results.html', {})

            else:
                return render(self.request, './templates/search_results.html', {})
