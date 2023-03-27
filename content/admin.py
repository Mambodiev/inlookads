from django.contrib import admin
from . import models

from .models import Course, Video, Pricing, Subscription, Sale


@admin.register(models.Course)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',), }

# admin.site.register(Course)
admin.site.register(Sale)
admin.site.register(Video)
admin.site.register(Pricing)
admin.site.register(Subscription)
