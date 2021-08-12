from django.contrib import admin
from .models import Genre, Movie

# added another column in the admin panel using class.ModelAdmin
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

# customize the admin interface movies table
class MovieAdmin(admin.ModelAdmin):
    exclude = ('date_created', )
    list_display = ('title', 'number_in_stock', 'daily_rate' )

admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
# Register your models here.
