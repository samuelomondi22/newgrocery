from django.urls import path
from .views import HomePageView, SearchResultsView, AddGrocery, GroceryDetail

urlpatterns = [
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('', HomePageView.as_view(), name='home'),
    path('add_grocery/', AddGrocery.as_view(), name='add_grocery'),
    path('detail/', GroceryDetail.as_view(), name='detail')
]
