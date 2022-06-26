from django.contrib import admin

from .models import ContactRequest, VolunteeringApplication , VolunteeringOpportunity
 
admin.site.register(VolunteeringOpportunity)
admin.site.register(VolunteeringApplication)
admin.site.register(ContactRequest)