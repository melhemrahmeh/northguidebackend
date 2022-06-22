from django.urls import path
from . import views

urlpatterns = [
    path('items/',views.getItems, name= "items"),
    path('items/create/', views.postItem, name = "item-create"),
    path('items/<str:pk>/',views.getItem, name = "item"),
    path('items/update/<str:pk>/', views.putItem, name="item-update"),
    path('items/delete/<str:pk>/', views.deleteItem, name="item-delete"),
    
    path('contactrequests/',views.getContactRequests, name= "contactrequests"),
    path('contactrequests/create/', views.postContactRequest, name = "contactrequest-create"),
    path('contactrequests/<str:pk>/',views.getContactRequest, name = "contactrequest"),
    path('contactrequests/update/<str:pk>/', views.putContactRequest, name="contactrequest-update"),
    path('contactrequests/delete/<str:pk>/', views.deleteContactRequest, name="contactrequest-delete"),
]