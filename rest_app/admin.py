from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

admin.site.register(models.User, UserAdmin)
admin.site.register(models.Category)
admin.site.register(models.Belonging)
admin.site.register(models.Post)
admin.site.register(models.Offer)
