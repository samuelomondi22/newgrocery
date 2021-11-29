from django.urls import path
from .views import HomePageView, SearchResultsView, SearchGrocery, GroceryDetail

urlpatterns = [
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('', HomePageView.as_view(), name='home'),
    path('add_grocery/', SearchGrocery.as_view(), name='add_grocery'),
    path('detail/', GroceryDetail.as_view(), name='detail')
]
