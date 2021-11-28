from django.urls import path
from .views import HomePageView, SearchResultsView, SearchGrocery, GroceryDetail, MallGrocery

urlpatterns = [
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('', HomePageView.as_view(), name='home'),
    path('add_grocery/', SearchGrocery.as_view(), name='add_grocery'),
    path('mall/', MallGrocery.as_view(), name='add_mall'),
    path('detail/', GroceryDetail.as_view(), name='detail')
]
