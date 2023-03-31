from django.contrib.auth import get_user_model
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import (
    OrderItem, Course
)

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': _("Your name")
    }), label=_('Name'))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'placeholder': _("Your e-mail")
    }), label=_('Email'))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': _('Your message')
    }), label=_('Message'))



class AddToCartForm(forms.ModelForm):
    # quantity = forms.IntegerField(min_value=1, initial=1, label=_('Quantity'))

    class Meta:
        model = OrderItem
        fields = ['quantity']

    def __init__(self, *args, **kwargs):
        self.course_id = kwargs.pop('course_id')
        course = Course.objects.get(id=self.course_id)
        super().__init__(*args, **kwargs)