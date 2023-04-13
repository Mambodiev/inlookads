from django.contrib.auth import get_user_model
from django import forms
from django.utils.translation import gettext_lazy as _


class ContactForm(forms.Form):
    # name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
    #     'placeholder': _("Your name")
    # }), label=_('Name'))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'placeholder': _("Your e-mail")
    }), label=_('Email'))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': _('Your message')
    }), label=_('Message'))