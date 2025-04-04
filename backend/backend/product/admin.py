from django.contrib import admin
from . models import *

# Register your models here.



class ItemAdmin(admin.ModelAdmin):
    list_display=('name','price', 'image', 'description', 'date')
    list_filter=('name', 'date')
    
    
    
admin.site.register(Item, ItemAdmin)
