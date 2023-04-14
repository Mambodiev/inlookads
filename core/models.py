from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model


User = get_user_model()


class Privacy(models.Model):

    privacy_text = RichTextUploadingField(blank=True, null=True,  help_text = "Privacy Policy Notice")
    name = models.CharField(max_length=100)  
    last_update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = ("Privacy")


class Terms(models.Model):

    terms_text = RichTextUploadingField(blank=True, null=True,  help_text = "User Terms and Conditions")
    name = models.CharField(max_length=100)  
    last_update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = ("Terms")


class Faq(models.Model):

    faq_text = RichTextUploadingField(blank=True, null=True,  help_text = "faq")
    name = models.CharField(max_length=100)  
    last_update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = ("Faq")


class About(models.Model):

    about_text = RichTextUploadingField(blank=True, null=True,  help_text = "about us")
    name = models.CharField(max_length=100)  
    last_update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = ("About")


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

