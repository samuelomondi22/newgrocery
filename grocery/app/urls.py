from django.urls import path
from .views import HomePageView, SearchResultsView, AddGrocery, GroceryDetail, success_view, failed_view

urlpatterns = [
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('', HomePageView.as_view(), name='home'),
    path('add_grocery/', AddGrocery.as_view(), name='add_grocery'),
    path('detail/', GroceryDetail.as_view(), name='detail'),
    path('success/', success_view, name='success'),
    path('failed/', failed_view, name='failed')
]
