from django.contrib import admin
from . import models

from .models import Course, Video, Pricing, Subscription, Sale, Store , OrderItem, Order


@admin.register(models.Course)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name_of_product']
    prepopulated_fields = {'slug': ('name_of_product',), }

# admin.site.register(Course)
admin.site.register(Store)
admin.site.register(Sale)
admin.site.register(Video)
admin.site.register(Pricing)
admin.site.register(Subscription)
admin.site.register(OrderItem)
admin.site.register(Order)