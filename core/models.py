from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


User = get_user_model()


class PrivacyTermsAbout(models.Model):

    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )

    privacy_text = RichTextUploadingField(blank=True, null=True,  help_text = "Privacy Policy Notice"),
    terms_text = RichTextUploadingField(blank=True, null=True,  help_text = "terms text"),
    about_text = RichTextUploadingField(blank=True, null=True,  help_text = "About text"),
    name = models.CharField(max_length=100), 
    status=models.CharField(max_length=10,choices=STATUS),
    update_at=models.DateTimeField(auto_now=True),
    last_update = models.DateTimeField(auto_now_add=True),

    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name_plural = ("PrivacyTermsAbout")





class Faq(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    ordernumber = models.IntegerField(null=True,)
    question = models.CharField(max_length=200, null=True,)
    answer = RichTextUploadingField(blank=True, null=True,)
    status=models.CharField(max_length=10, choices=STATUS, null=True,)
    create_at=models.DateTimeField(auto_now_add=True, null=True, )
    update_at=models.DateTimeField(auto_now=True, null=True, )

    def __str__(self):
        return self.question

    class Meta:
        verbose_name_plural = ("Faq")


class Price(models.Model):

    price_text = RichTextUploadingField(blank=True, null=True,  help_text = "price")
    name = models.CharField(max_length=100)  
    last_update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = ("Price")



class Affiliate(models.Model):

    affiliate_text = RichTextUploadingField(blank=True, null=True,  help_text = "Affiliate")
    name = models.CharField(max_length=100)  
    last_update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
