from django.contrib import admin
from rango.models import Category, Page

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

# Ccustomise the Admin Interface 
class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}

# Register your models here.
admin.site.register(Page, PageAdmin)
admin.site.register(Category, CategoryAdmin)