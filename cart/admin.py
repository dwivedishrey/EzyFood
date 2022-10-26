from distutils.sysconfig import customize_compiler
from django.contrib import admin

from cart.models import Food, Hotels, message ,Customize , Dal , Roti , Sabji

# Register your models here.

admin.site.register(Hotels)
admin.site.register(message)
admin.site.register(Food)
admin.site.register(Customize)
admin.site.register(Roti)
admin.site.register(Dal)
admin.site.register(Sabji)