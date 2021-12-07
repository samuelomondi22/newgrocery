from django.shortcuts import redirect, render
from django.views.generic import TemplateView, ListView
from .models import Grocery, Mall
from django.db.models import Q
from django.contrib import messages

# Create your views here.


class HomePageView(TemplateView):
    template_name = 'home.html'

class GroceryDetail(TemplateView):
    template_name = 'detail.html'
    
class SearchGrocery(TemplateView):
    template_name = 'add_grocery.html'

    # retrieve and check if the item_name exist if it does call the add mall function is not then this function below is called
    def post(self):
        if self.request.method == 'POST':
            if self.request.POST.get('item_name') and self.request.POST.get('item_price') and self.request.POST.get('item_mall'):
                item_name = self.request.POST.get('item_name')
                grocery = Grocery(
                    item_name=item_name)
                grocery.save()
                item_price = self.request.POST.get('item_price')
                item_mall = self.request.POST.get('item_mall')  
                grocery.mall_set.create(item_price=item_price, item_mall=item_mall, grocery=grocery)
                grocery.save()
                messages.success(self.request, "Item Added Successfully")

                return redirect('/')

            else:
                return redirect('/')


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
    
    def post(self):
        grocery = self.get_queryset()
        if self.request.method == 'POST':
            if self.request.POST.get('item_price') and self.request.POST.get('item_mall'):
                item_price = self.request.POST.get('item_price')
                item_mall = self.request.POST.get('item_mall')
                mall = Mall(item_price=item_price, item_mall=item_mall, grocery=grocery)
                mall.save()
                messages.success(self.request, "Mall Added Successfully")

                return redirect('search_results.html')

            else:
                return redirect('search_results.html')

            
