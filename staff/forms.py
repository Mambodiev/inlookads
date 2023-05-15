from django import forms

from content.models import Course, Category, Technology, Country, Language, Button

class ProductForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = (
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
            # 'links_to_ads',
            'text_that_comes_with_ads',
            'number_of_store_selling',
            'number_of_suppliers_selling',
            'created_at',
            'countries',
            'technologies',
            'languages',
            'buttons',
            # 'links_to_others_stores',
            # 'links_to_others_suppliers',
            'is_faceBook',
            'is_pinterest',
            'is_tiktok',
            'has_video',
            'has_photo',
            'slug',
        )


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class TechnologyForm(forms.ModelForm):
    class Meta:
        model = Technology
        fields = ['name']


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['name']



class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ['name']


class ButtonForm(forms.ModelForm):
    class Meta:
        model = Button
        fields = ['name']