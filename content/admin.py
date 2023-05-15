from modeltranslation.admin import TranslationAdmin
import admin_thumbnails
from django.utils.html import format_html
from django.contrib import admin
from . import models
from .models import Course, Category, Video, Pricing, Subscription, Sale, Store , OrderItem, Order, Country, Technology, Language, Button, City, OtherShopifyLinks, OtherAliexpressSuppliersLinks



class PricingAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')


@admin.register(models.Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')


class SaleAdmin(admin.ModelAdmin):
    list_display = ('course', 'total_number_of_sale', 'time', 'created_at', 'updated_at')



class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')


class PricingAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'pricing', 'status', 'created_at', 'updated_at')


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'course', 'created_at', 'updated_at')



class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'start_date')



class CourseAdmin(TranslationAdmin):
    list_display = ('name_of_product', 'created_at', 'updated_at','buttons', 'countries','img_preview')
    readonly_fields = ['img_preview']

    def get_prepopulated_fields(self, request, obj=None):
        return {
        'slug_en': ('name_of_product_en',),
        'slug_fr': ('name_of_product_fr',),
        }


class CategoryAdmin(TranslationAdmin):
    list_display = ('name', 'created_at', 'updated_at')


class TechnologyAdmin(TranslationAdmin):
    list_display = ('name', 'created_at', 'updated_at')


class CountryAdmin(TranslationAdmin):
    list_display = ('name', 'created_at', 'updated_at')


class LanguageAdmin(TranslationAdmin):
    list_display = ('name', 'created_at', 'updated_at')


class ButtonAdmin(TranslationAdmin):
    list_display = ('name', 'created_at', 'updated_at')

class CityAdmin(TranslationAdmin):
    list_display = ('name', )


# class OtherShopifyLinksAdmin(admin.ModelAdmin):
#     list_display = ('name', 'country')


class OtherAliexpressSuppliersLinksAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')


admin.site.register(OtherAliexpressSuppliersLinks, OtherAliexpressSuppliersLinksAdmin)
admin.site.register(OtherShopifyLinks)
admin.site.register(Course, CourseAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Technology, TechnologyAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Button, ButtonAdmin)
admin.site.register(Sale, SaleAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Pricing, PricingAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Order, OrderAdmin)