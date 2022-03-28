from django.contrib import admin
from .models import Recipe, Nutrient

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Nutrient)
