from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.User)
admin.site.register(models.Category)
admin.site.register(models.Products)
admin.site.register(models.Order)
admin.site.register(models.UserType)