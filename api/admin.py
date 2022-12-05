from django.contrib import admin

from .models import Location, Place, Tourist

admin.site.register(Tourist)
admin.site.register(Place)
admin.site.register(Location)
