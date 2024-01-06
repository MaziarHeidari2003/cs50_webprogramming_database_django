from django.contrib import admin
from .models import Passengers,Flight, Airport

# Register your models here.

admin.site.register(Airport)
admin.site.register(Flight)
admin.site.register(Passengers)