from django.contrib import admin
from demo.models import Publisher, Author, Book, City, Area, Province


# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date')
    list_filter = ('publication_date',)
    date_hierarchy = 'publication_date'


class CityAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')
    search_fields = ('name',)


class AreaAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')
    search_fields = ('name',)


class ProvinceAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')
    search_fields = ('name',)


admin.site.register(Publisher)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(Province, ProvinceAdmin)
