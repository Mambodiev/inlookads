from django import forms
from parler.admin import TranslatableModelForm

from content.models import Course, Category, Technology, Country, Language, Button

class ProductForm(TranslatableModelForm):
    class Meta:
        model = Course
        fields = [
            'name_of_store',
            'shopify_links',
            'name_of_product',
            'shopify_price',
            'product_thumbnail',
            'store_logo',
            'aliexpress_order',
            'aliexpress_price',
            'categories',
            'likes',
            'comment',
            'views',
            'links_to_ads',
            'text_that_comes_with_ads',
            'number_of_store_selling',
            'number_of_suppliers_selling',
            'created_at',
            'countries',
            'technologies',
            'languages',
            'buttons',
            'links_to_others_stores',
            'links_to_others_suppliers',
            'is_faceBook',
            'is_pinterest',
            'is_tiktok',
            'has_video',
            'has_photo',
            'slug',
        ]


class CategoryForm(TranslatableModelForm):
    class Meta:
        model = Category
        fields = ['name']


class TechnologyForm(TranslatableModelForm):
    class Meta:
        model = Technology
        fields = ['name']


class CountryForm(TranslatableModelForm):
    class Meta:
        model = Country
        fields = ['name']



class LanguageForm(TranslatableModelForm):
    class Meta:
        model = Language
        fields = ['name']


class ButtonForm(TranslatableModelForm):
    class Meta:
        model = Button
        fields = ['name']