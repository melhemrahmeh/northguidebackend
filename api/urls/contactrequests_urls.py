from django.urls import path
from api.views import contactrequests_views as views

urlpatterns = [
    path('',views.getContactRequests, name= "items"),
    path('create/', views.postContactRequest, name = "item-create"),
    path('<str:pk>/',views.getContactRequest, name = "item"),
    path('update/<str:pk>/', views.putContactRequest, name="item-update"),
    path('delete/<str:pk>/', views.deleteContactRequest, name="item-delete"),    
]