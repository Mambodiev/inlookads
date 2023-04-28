import admin_thumbnails
from django.utils.html import format_html
from django.contrib import admin
from parler.admin import TranslatableAdmin
from . import models
from .models import Course, Video, Pricing, Subscription, Sale, Store , OrderItem, Order, Category, Country, Technology, Language, Button



# @admin.register(Course) 
# class CourseAdmin(TranslatableAdmin):
#     list_display = ['name_of_product','categories', 'technologies', 'buttons', 'countries','img_preview']
#     readonly_fields = ['img_preview']

#     def get_prepopulated_fields(self, request, obj=None):
#         return {
#             'slug': ('name_of_product',)
#         }



class PricingAdmin(TranslatableAdmin):
    list_display = ('name', 'created_at', 'updated_at')


class CategoryAdmin(TranslatableAdmin):
    list_display = ('name', 'created_at', 'updated_at')


class CountryAdmin(TranslatableAdmin):
    list_display = ('name', 'created_at', 'updated_at')


class TechnologyAdmin(TranslatableAdmin):
    list_display = ('name', 'created_at', 'updated_at')


class LanguageAdmin(TranslatableAdmin):
    list_display = ('name', 'created_at', 'updated_at')


class ButtonAdmin(TranslatableAdmin):
    list_display = ('name', 'created_at', 'updated_at')

@admin.register(models.Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')


class SaleAdmin(TranslatableAdmin):
    list_display = ('course', 'created_at', 'updated_at')


class VideoAdmin(TranslatableAdmin):
    list_display = ('title', 'created_at', 'updated_at')


class PricingAdmin(TranslatableAdmin):
    list_display = ('name', 'created_at', 'updated_at')


class SubscriptionAdmin(TranslatableAdmin):
    list_display = ('user', 'pricing', 'status', 'created_at', 'updated_at')


class OrderItemAdmin(TranslatableAdmin):
    list_display = ('order', 'course', 'created_at', 'updated_at')



class OrderAdmin(TranslatableAdmin):
    list_display = ('user', 'start_date')


class CourseAdmin(TranslatableAdmin):
    list_display = ('name_of_product', 'created_at', 'updated_at','buttons', 'countries','img_preview')
    readonly_fields = ['img_preview']

    # fieldsets = (
    #     (None, {
    #         'fields': ('slug', 'name_of_product', 'created_at', 'updated_at','buttons', 'countries','img_preview'),
    #     }),
    # )

    def get_prepopulated_fields(self, request, obj=None):
        return {
            'slug': ('name_of_product',)
        }
    # fieldsets = (
    #     (None, {
    #         'fields': ('slug', 'name_of_product', 'categories'),
    #     }),
    # )





admin.site.register(Course, CourseAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Technology, TechnologyAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Button, ButtonAdmin)
# admin.site.register(Store,StoreAdmin)
admin.site.register(Sale, SaleAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Pricing, PricingAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Order, OrderAdmin)