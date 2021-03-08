
# I created admin.py to test and observe the tables created in django admin site.Below are all the tables we registered.

from django.contrib import admin
from homes.models import *

admin.site.register(House)
admin.site.register(Thermostat)
admin.site.register(Room)
admin.site.register(Light)