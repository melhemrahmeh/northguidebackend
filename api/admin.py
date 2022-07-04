from django.contrib import admin

from .models import ContactRequest, VolunteeringApplication , VolunteeringOpening
 
admin.site.register(VolunteeringOpening)
admin.site.register(VolunteeringApplication)
admin.site.register(ContactRequest)