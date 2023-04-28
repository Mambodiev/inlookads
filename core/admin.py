from django.contrib import admin
from parler.admin import TranslatableAdmin
from . import models
from .models import PrivacyTermsAbout, Faq, Price, Affiliate


class PrivacyTermsAboutAdmin(TranslatableAdmin):
    list_display = ('name', 'status', 'update_at', 'last_update')
    readonly_fields=('update_at', 'last_update')

admin.site.register(PrivacyTermsAbout, PrivacyTermsAboutAdmin)
admin.site.register(Faq)
admin.site.register(Price)
admin.site.register(Affiliate)