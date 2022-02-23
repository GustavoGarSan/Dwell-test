from django.contrib import admin

# Register your models here.
from .models import Restaurant, Ticket

admin.site.register(Restaurant)
admin.site.register(Ticket)