from django.contrib import admin

from .models import Stock, Place, Worker
#
admin.site.register(Stock)
admin.site.register(Place)
admin.site.register(Worker)
