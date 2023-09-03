from django.contrib import admin
from django.contrib.auth.models import User
from . import models

class ProfileInline(admin.StackedInline):
    model = models.Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"]
    inlines = [ProfileInline]

admin.site.register(models.UserPost)
admin.site.unregister(User)
admin.site.register(models.Comment)
admin.site.register(models.Like)
admin.site.register(models.Profile)



