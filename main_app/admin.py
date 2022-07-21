from curses.ascii import SP
from django.contrib import admin
from .models import Sportbike, Photo

# Register your models here.
admin.site.register(Sportbike)
admin.site.register(Photo)