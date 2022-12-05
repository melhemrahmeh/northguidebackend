from django.urls import path
from api.views import places_views as views

urlpatterns = [
    path('', views.getPlaces, name="items"),
    path('create/', views.postPlace, name="item-create"),
    path('<str:pk>/', views.getPlace, name="item"),
    path('update/<str:pk>/', views.putPlace, name="item-update"),
    path('delete/<str:pk>/', views.deletePlace, name="item-delete"),
]
