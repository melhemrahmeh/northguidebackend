from django.urls import path
from api.views import users_views as views

urlpatterns = [
    path('', views.getTourists, name="items"),
    path('create/', views.postTourist, name="item-create"),
    path('<str:pk>/', views.getTourist, name="item"),
    path('update/<str:pk>/', views.putTourist, name="item-update"),
    path('delete/<str:pk>/', views.deleteTourist, name="item-delete"),
]
