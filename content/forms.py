from django.contrib.auth import get_user_model
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import (
    OrderItem, Course
)



class AddToCartForm(forms.ModelForm):
    quantity = forms.IntegerField(min_value=1, initial=1, label=_('Quantity'))

    class Meta:
        model = OrderItem
        fields = ['quantity']

    def __init__(self, *args, **kwargs):
        self.course_id = kwargs.pop('course_id')
        course = Course.objects.get(id=self.course_id)
        super().__init__(*args, **kwargs)