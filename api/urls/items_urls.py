from django.urls import path
from api.views import items_views as views

urlpatterns = [
    path('',views.getItems, name= "items"),
    path('create/', views.postItem, name = "item-create"),
    path('<str:pk>/',views.getItem, name = "item"),
    path('update/<str:pk>/', views.putItem, name="item-update"),
    path('delete/<str:pk>/', views.deleteItem, name="item-delete"),    
]