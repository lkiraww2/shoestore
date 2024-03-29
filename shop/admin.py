from django.contrib import admin
from shop.models import Shoe
from django.db import models
# Register your models here.
class AdminBacl(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("static/src/admin.css",)
        }
        
class ShoeAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'color', 'size', 'price')
    search_fields = ('name', 'brand', 'color')

admin.site.register(Shoe,ShoeAdmin)
admin.site.site_header = "base.html"