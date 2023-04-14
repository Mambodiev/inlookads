from django.contrib import admin
from . import models

from .models import Privacy, Terms, Faq, About, Price, Affiliate

admin.site.register(Privacy)
admin.site.register(Terms)
admin.site.register(Faq)
admin.site.register(About)
admin.site.register(Price)
admin.site.register(Affiliate)