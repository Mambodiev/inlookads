from django.contrib import admin
from . import models

from .models import PrivacyTermsAbout, Faq, Price, Affiliate, PrivacyTermsAboutLang, AffiliateLang, PriceLang, Language

class PrivacyTermsAboutLangAdmin(admin.ModelAdmin):
    list_display = ['name','lang', 'update_at', 'create_at' ]

class AffiliateLangAdmin(admin.ModelAdmin):
    list_display = ['name','lang', 'update_at', 'create_at' ]

class PriceLangAdmin(admin.ModelAdmin):
    list_display = ['name','lang', 'update_at', 'create_at' ]

class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name', 'code','status']
    list_filter = ['status']

admin.site.register(PrivacyTermsAbout)
admin.site.register(Faq)
admin.site.register(Price)
admin.site.register(Affiliate)
admin.site.register(PrivacyTermsAboutLang, PrivacyTermsAboutLangAdmin)
admin.site.register(AffiliateLang, AffiliateLangAdmin)
admin.site.register(PriceLang,PriceLangAdmin)
admin.site.register(Language,LanguageAdmin)
