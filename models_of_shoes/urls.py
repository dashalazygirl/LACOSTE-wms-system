from django.contrib import admin
from django.urls import path
from .views import index, add, models_of_shoes, delete_model, find_articul,find_size, ShoesDetailView


app_name = 'models_of_shoes'
urlpatterns = [
    path('', index, name='index'),
    path('add/', models_of_shoes, name='add'),
    path('<int:pk>/edit/',models_of_shoes, name='edit'),
    path('<int:pk>/delete/',delete_model, name='delete'),
    path('find_articul/', find_articul, name = 'find_articul'),
    path('find_size/', find_size, name = 'find_size'),
    path('<int:pk>/detail/', ShoesDetailView.as_view(), name = 'detail')
]


