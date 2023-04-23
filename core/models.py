from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model


User = get_user_model()


class Language(models.Model):
    name= models.CharField(max_length=20)
    code= models.CharField(max_length=5)
    status=models.BooleanField()
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


llist = Language.objects.filter(status=True)
list1 = []
for rs in llist:
    list1.append((rs.code,rs.name))
langlist = (list1)



class PrivacyTermsAbout(models.Model):

    privacy_text = RichTextUploadingField(blank=True, null=True,  help_text = "Privacy Policy Notice")
    Terms_text = RichTextUploadingField(blank=True, null=True,  help_text = "Privacy Policy Notice")
    About_text = RichTextUploadingField(blank=True, null=True,  help_text = "Privacy Policy Notice")
    name = models.CharField(max_length=100)  
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = ("PrivacyTermsAbout")


# class Terms(models.Model):

#     terms_text = RichTextUploadingField(blank=True, null=True,  help_text = "User Terms and Conditions")
#     name = models.CharField(max_length=100)  
#     create_at=models.DateTimeField(auto_now_add=True)
    # update_at=models.DateTimeField(auto_now=True)


#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name_plural = ("Terms")

# class About(models.Model):

    # about_text = RichTextUploadingField(blank=True, null=True,  help_text = "about us")
    # name = models.CharField(max_length=100)  
    # create_at=models.DateTimeField(auto_now_add=True)
    # update_at=models.DateTimeField(auto_now=True)


    # def __str__(self):
    #     return self.name

    # class Meta:
    #     verbose_name_plural = ("About")


class Price(models.Model):

    price_text = RichTextUploadingField(blank=True, null=True,  help_text = "price")
    name = models.CharField(max_length=100)  
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = ("Price")



class Affiliate(models.Model):

    affiliate_text = RichTextUploadingField(blank=True, null=True,  help_text = "Affiliate")
    name = models.CharField(max_length=100)  
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name


# internationalization


class PrivacyTermsAboutLang(models.Model):
    privacy_terms_about = models.ForeignKey(PrivacyTermsAbout, on_delete=models.CASCADE) 
    lang =  models.CharField(max_length=6, choices=langlist)
    privacy_text = RichTextUploadingField(blank=True, null=True,  help_text = "Privacy Policy Notice")
    Terms_text = RichTextUploadingField(blank=True, null=True,  help_text = "Privacy Policy Notice")
    About_text = RichTextUploadingField(blank=True, null=True,  help_text = "Privacy Policy Notice")
    name = models.CharField(max_length=100) 
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
 

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = ("PrivacyTermsAboutLang")




class AffiliateLang(models.Model):
    affiliate = models.ForeignKey(Affiliate, on_delete=models.CASCADE) 
    lang =  models.CharField(max_length=6, choices=langlist)
    affiliate_text = RichTextUploadingField(blank=True, null=True,  help_text = "Affiliate")
    name = models.CharField(max_length=100)  
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name


class PriceLang(models.Model):
    price = models.ForeignKey(Price, on_delete=models.CASCADE) 
    lang =  models.CharField(max_length=6, choices=langlist)
    price_text = RichTextUploadingField(blank=True, null=True,  help_text = "price")
    name = models.CharField(max_length=100)  
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = ("PriceLang")


class Faq(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    lang =  models.CharField(max_length=6, choices=langlist, blank=True, null=True)
    ordernumber = models.IntegerField(blank=True, null=True, )
    question = models.CharField(blank=True, null=True, max_length=200)
    answer = RichTextUploadingField(blank=True, null=True, )
    status=models.CharField(blank=True, null=True, max_length=10, choices=STATUS)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question