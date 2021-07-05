from .views import *
from django.urls import path

urlpatterns = [
    path('', home, name='home'),
    path('list_item/', list_item, name='list_item'),
    path('add_items/', add_items, name='add_items'),
]
