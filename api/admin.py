from django.contrib import admin

from .models import ContactRequests, VolunteeringApplications , VolunteeringOpportunities ,Items

admin.site.register(Items)
admin.site.register(VolunteeringApplications)
admin.site.register(VolunteeringOpportunities)
admin.site.register(ContactRequests)