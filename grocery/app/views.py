from django.db.models.query import InstanceCheckMeta
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import Grocery, Mall
from django.db.models import Q, fields
from django.forms import ModelForm
from .forms import MallForm, GroceryForm
import datetime as dt
from django.template import RequestContext
from django.http import HttpResponse
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
                # grocery = Grocery()
                # mall = Mall()
                # grocery.item_name = self.request.POST.get('item_name')
                # grocery.item_comment = self.request.POST.get('item_comment')
                # grocery.item_rate = self.request.POST.get('item_rate')
                # grocery.save()
                # date = self.request.POST.get('date')
                # item_price = self.request.POST.get('item_price')
                # item_mall = self.request.POST.get('item_mall')
                # grocery.mall_set.create(
                #     date=date, item_price=item_price, item_mall=item_mall, grocery=grocery)
                item_name = self.request.POST.get('item_name')
                if Grocery.objects.filter(item_name=item_name) == item_name:
                    messages.error(self.request, "Item Already exists in the database")
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
                messages.success(self.request, "Item Added")

                return render(request, '../templates/add_grocery.html', {})

            else:
                return render(request, '../templates/add_grocery.html', {})


class SearchPage(TemplateView):
    template_name = 'searchpage.html'

class SearchResultsView(ListView):
    template_name = 'search_results.html'
    
    def get_queryset(self): 
        query = self.request.GET.get('q')
        object_list = Grocery.objects.get(
            Q(item_name__icontains=query) 
            # | Q(state__icontains=query)
        ).mall_set.all()
        return object_list



