from django.urls import path
from api.views import volunteeringapplications_views as views

urlpatterns = [
    path('',views.getVolunteeringApplications, name= "items"),
    path('create/', views.postVolunteeringApplication, name = "item-create"),
    path('<str:pk>/',views.getVolunteeringApplication, name = "item"),
    path('update/<str:pk>/', views.putVolunteeringApplication, name="item-update"),
    path('delete/<str:pk>/', views.deleteVolunteeringApplication, name="item-delete"),    
]