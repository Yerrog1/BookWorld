from django.contrib import admin
from .models import *

class BookAdmin(admin.ModelAdmin):
    list_display = ('isbn', 'title', 'author', 'genre', 'price', 'image')

    list_filter = ('genre', 'author')
    search_fields = ('title', 'author')
    ordering = ('title',)
    filter_horizontal = ()
    list_per_page = 10

class AuthorAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'description')
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
    filter_horizontal = ()
    list_per_page = 10
class UserAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'email')
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
    filter_horizontal = ()
    list_per_page = 10


admin.site.register(User, UserAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)