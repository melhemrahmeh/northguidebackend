from django.urls import path
from api.views import volunteeringopportunities_views as views

urlpatterns = [
    path('',views.getVolunteeringOpportunities, name= "items"),
    path('create/', views.postVolunteeringOpportunity, name = "item-create"),
    path('<str:pk>/',views.getVolunteeringOpportunity, name = "item"),
    path('update/<str:pk>/', views.putVolunteeringOpportunity, name="item-update"),
    path('delete/<str:pk>/', views.deleteVolunteeringOpportunity, name="item-delete"),    
]