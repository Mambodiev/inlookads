from django.contrib import admin
from . import models

from .models import Privacy, Terms, Faq

admin.site.register(Privacy)
admin.site.register(Terms)
admin.site.register(Faq)