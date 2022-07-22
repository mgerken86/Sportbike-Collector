from curses.ascii import SP
from django.contrib import admin
from .models import Sportbike, Trim, Photo, Colors

# Register your models here.
admin.site.register(Sportbike)
admin.site.register(Trim)
admin.site.register(Colors)
admin.site.register(Photo)