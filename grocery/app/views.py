from django.shortcuts import redirect, render
from django.views.generic import TemplateView, ListView, UpdateView
from .models import Grocery, Mall
from django.db.models import Q
from django.contrib import messages
from django.conf import settings

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

class GroceryDetail(TemplateView):
    template_name = 'detail.html'
    
class AddGrocery(UpdateView):
    template_name = 'add_grocery.html'

    # retrieve and check if the item_name exist if it does call the add mall function is not then this function below is called
    def post(self, request):
        if self.request.method == 'POST':
            # validates that we have values for each of the required fields
            if self.request.POST.get('item_name') and  self.request.POST.get('item_price') and self.request.POST.get('item_mall'):
                new_item_name = self.request.POST.get('item_name')
                # add a self check
                new_item_price = self.request.POST.get('item_price')
                new_item_mall = self.request.POST.get('item_mall')
                if Grocery.objects.filter(item_name=new_item_name).exists():
                    return redirect('')
                else:
                    new_grocery = Grocery(item_name=new_item_name)
                    new_grocery.save()
                    # mall_set is built in function, saves the mall items with the accsiated new_grocery
                    new_grocery.mall_set.create(item_price=new_item_price, item_mall=new_item_mall, grocery=new_grocery)
                    new_grocery.save()
                

                # stores the message in the database
                messages.success(self.request, "Item Added Successfully")

                return redirect('add_grocery')
            else:
                return redirect('add_grocery')


class NoGrocery(TemplateView):
    template_name = 'modalsection.html'

class SearchResultsView(ListView):
    template_name = 'search_results.html'
    # have this give a pop up message if the item searched for isn't there and give an option of continue to search or add
    # the item
    def get_queryset(self): 
        query = self.request.GET.get('q')

        # This checks if the searched grocery exists
        if Grocery.objects.filter(item_name=query).exists():
            object_list = Grocery.objects.get(Q(item_name__icontains=query))
            return object_list
     
    
    # This function allows you to post a mall, has nothing to do with groceries
    def post(self, request):
        grocery = self.get_queryset()
        if self.request.method == 'POST':
            
            if self.request.POST.get('item_price') and self.request.POST.get('item_mall'):
                new_item_price = self.request.POST.get('item_price')
                new_item_mall = self.request.POST.get('item_mall')
                
                mall = Mall(item_price=new_item_price, item_mall=new_item_mall, grocery=grocery)
                mall.save()

                messages.success(self.request, "Mall Added Successfully")

                return redirect('search_results.html')
            else:
                return redirect('search_results.html')

            
