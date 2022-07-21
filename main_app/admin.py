from curses.ascii import SP
from django.contrib import admin
from .models import Sportbike, Trim, Photo

# Register your models here.
admin.site.register(Sportbike)
admin.site.register(Trim)
admin.site.register(Photo)