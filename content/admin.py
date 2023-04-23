import admin_thumbnails
from django.utils.html import format_html

from django.contrib import admin
from . import models

from .models import Course, Video, Pricing, Subscription, Sale, Store , OrderItem, Order, Category, Country, Technology, Language, Button



@admin.register(Course) 
class CourseAdmin(admin.ModelAdmin):
    list_filter = ['buttons', 'countries' ]
    list_display = ['name_of_product','categories', 'technologies', 'buttons', 'countries','img_preview']
    readonly_fields = ['img_preview']
    prepopulated_fields = {'slug': ('name_of_product',), }



admin.site.register(Category)
admin.site.register(Country)
admin.site.register(Technology)
admin.site.register(Language)
admin.site.register(Button)
admin.site.register(Store)
admin.site.register(Sale)
admin.site.register(Video)
admin.site.register(Pricing)
admin.site.register(Subscription)
admin.site.register(OrderItem)
admin.site.register(Order)