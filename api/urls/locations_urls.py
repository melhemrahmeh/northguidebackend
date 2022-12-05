from django.urls import path
from api.views import locations_views as views

urlpatterns = [
    path('', views.getLocations, name="items"),
    path('create/', views.postLocation, name="item-create"),
    path('<str:pk>/', views.getLocation, name="item"),
    path('update/<str:pk>/', views.putLocation, name="item-update"),
    path('delete/<str:pk>/', views.deleteLocation, name="item-delete"),
]
