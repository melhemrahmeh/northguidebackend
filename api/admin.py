from django.contrib import admin

from .models import ContactRequest, VolunteeringForm

admin.site.register(ContactRequest)
admin.site.register(VolunteeringForm)