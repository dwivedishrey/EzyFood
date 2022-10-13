from django.contrib import admin

from cart.models import Food, Hotels, message

# Register your models here.

admin.site.register(Hotels)
admin.site.register(message)
admin.site.register(Food)
