from django.contrib import admin

# Register your models here.
from film.models import Genre,Language,Actors,Movies
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Actors)
admin.site.register(Movies)