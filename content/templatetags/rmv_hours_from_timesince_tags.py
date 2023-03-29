from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def upto_tags(value, delimiter=None):
    return value.split(delimiter)[0]
upto_tags.is_safe = True