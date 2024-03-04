from django.contrib import admin
from . models import *
from .models import kylie,Lakme,MAC,Nykaa

admin.site.register(Account_Details)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'image_url', 'description']
    list_display_links = ['name']
    search_fields = ['name', 'description']
    list_filter = ['price']
    list_per_page = 20
# project 1
admin.site.register(kylie, ProductAdmin)
admin.site.register(Lakme,ProductAdmin)
admin.site.register(MAC,ProductAdmin)
admin.site.register(Nykaa,ProductAdmin)




#project 2
