from django.contrib import admin
from .models import Attendee, Category, Event

admin.site.register(Attendee)
admin.site.register(Category)
admin.site.register(Event)
