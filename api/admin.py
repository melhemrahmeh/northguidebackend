from django.contrib import admin

from .models import ContactRequest, VolunteeringApplication , VolunteeringOpportunity ,Item

admin.site.register(Item)
admin.site.register(VolunteeringApplication)
admin.site.register(VolunteeringOpportunity)
admin.site.register(ContactRequest)