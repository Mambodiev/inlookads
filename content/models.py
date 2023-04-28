from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, post_save
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify
from django.shortcuts import reverse, get_object_or_404
from django.contrib.auth import get_user_model
from allauth.account.signals import email_confirmed
import stripe
from django.utils.html import mark_safe
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

# stripe.api_key = settings.STRIPE_SECRET_KEY

User = get_user_model()


class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return timezone.now()

class Pricing(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(_('name'), max_length=100),# Basic / Pro / Premium
        )
    created_at = models.DateField(default=timezone.now),
    updated_at = AutoDateTimeField(default=timezone.now)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = ("Prices")

class Subscription(TranslatableModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE),
    pricing = models.ForeignKey(Pricing, on_delete=models.CASCADE, related_name='subscriptions'),
    stripe_subscription_id = models.CharField(_('stripe_subscription_id'), max_length=50),
    status = models.CharField(_('status'), max_length=100),
    created_at = models.DateField(default=timezone.now),
    updated_at = AutoDateTimeField(default=timezone.now)
        

    def __str__(self):
        return self.user.email


# class Course(TranslatableModel):
#     pricing_tiers = models.ManyToManyField(Pricing, blank=True)
#     name = models.CharField(_(''), max_length=100)
#     slug = models.SlugField(_(''), unique=True)
#     thumbnail = models.ImageField(_(''), upload_to="thumbnails/")
#     call_to_action = RichTextUploadingField(_(''), blank=True, null=True,)
#     description = RichTextUploadingField(_(''), blank=True, null=True,)

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse("content:course-detail", kwargs={"slug": self.slug})

class Store(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateField(default=timezone.now)
    updated_at = AutoDateTimeField(default=timezone.now)    
        
    def __str__(self):
        return self.name

 
class Category(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(_('name'), max_length=100),
        )
    created_at = models.DateField(default=timezone.now),
    updated_at = AutoDateTimeField(default=timezone.now) 
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Technology(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(_('name'), max_length=100),
        )
    created_at = models.DateField(default=timezone.now),
    updated_at = AutoDateTimeField(default=timezone.now) 
    class Meta:
        verbose_name_plural = ("Technologies")

    def __str__(self):
        return self.name


class Country(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(_('name'), max_length=100),
        )
    created_at = models.DateField(default=timezone.now),
    updated_at = AutoDateTimeField(default=timezone.now) 
    class Meta:
        verbose_name_plural = ("Countries")

    def __str__(self):
        return self.name


class Language(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(_('name'), max_length=100),
        )
    created_at = models.DateField(default=timezone.now),
    updated_at = AutoDateTimeField(default=timezone.now) 
    class Meta:
        verbose_name_plural = ("Languages")

    def __str__(self):
        return self.name

    


class Button(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(_('name'), max_length=100),
        )
    created_at = models.DateField(default=timezone.now),
    updated_at = AutoDateTimeField(default=timezone.now) 
    class Meta:
        verbose_name_plural = ("Buttons")

    def __str__(self):
        return self.name


class Course(TranslatableModel):

    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    translations = TranslatedFields(
        
        name_of_product = models.CharField(_('name_of_product'), max_length=100),
        slug = models.SlugField(_('slug'), unique=True),
        
    )
    shopify_links = models.CharField(blank=True, null=True, max_length=500, help_text = "A link that will take to a single the store")
    name_of_store = models.ForeignKey(Store, related_name='store_name', blank=True, null=True, on_delete=models.PROTECT)
    categories = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE)
    technologies = models.ForeignKey(Technology, related_name='store_name', blank=True, null=True, on_delete=models.PROTECT)
    shopify_price = models.DecimalField(_('shopify_price'), max_digits=10, decimal_places=2, help_text = "Product price from shopify")
    product_thumbnail = models.ImageField(_('product_thumbnail'), upload_to="thumbnails/", default='products/defaut_image_store_light_blue_bag.jpg')
    store_logo = models.ImageField(_('store_logo'), upload_to="image_store/",default='products/defaut_image_store.png',
            blank=True)
    aliexpress_order = models.IntegerField(_('aliexpress_order'), default=0, help_text = "Amount of aliexpress order generated")
    aliexpress_price = models.DecimalField(_('aliexpress_price'), max_digits=10, decimal_places=2, help_text = "Product price from aliexpress")
    likes = models.IntegerField(_('likes'), default=0, help_text = "Amount of likes generated")
    comment = models.IntegerField(_('comment'), default=0, help_text = "Amount of comment generated")
    views = models.IntegerField(_('views'), default=0, help_text = "Amount of views generated")
    links_to_ads = RichTextUploadingField(_('links_to_ads'), blank=True, null=True,  help_text = "A link that will take to ads")
    text_that_comes_with_ads = RichTextUploadingField(_('text_that_comes_with_ads'), blank=True, null=True)
    number_of_store_selling = models.IntegerField(_('number_of_store_selling'), default=0, help_text = "Amount of store selling the product")
    number_of_suppliers_selling= models.IntegerField(_('number_of_suppliers_selling'), default=0, help_text = "Amount of suppliers selling the product")
    created_at = models.DateField(default=timezone.now)
    languages = models.ForeignKey(Language, related_name='store_name', blank=True, null=True, on_delete=models.PROTECT)
    buttons = models.ForeignKey(Button, related_name='store_name', blank=True, null=True, on_delete=models.PROTECT)
    countries = models.ForeignKey(Country, blank=True, null=True, on_delete=models.PROTECT)
    links_to_others_stores = RichTextUploadingField(_('links_to_others_stores'), blank=True, null=True,help_text = "A link that will take to the store", )
    links_to_others_suppliers = RichTextUploadingField(_('links_to_others_suppliers'), blank=True, null=True,)
    is_faceBook = models.BooleanField(_('is_faceBook'), default=False)
    is_pinterest = models.BooleanField(_('is_pinterest'), default=False)
    is_tiktok = models.BooleanField(_('is_tiktok'), default=False)
    has_video = models.BooleanField(_('has_video'), default=False)
    has_photo = models.BooleanField(_('has_photo'), default=False)
    price_margin = models.DecimalField(_('price_margin'), max_digits=10, decimal_places=2, help_text = "Profit you get from this product", blank=True)
    updated_at = AutoDateTimeField(default=timezone.now)
    aliexpress_total_sale = models.DecimalField(max_digits=10, decimal_places=2, help_text = "Amount of aliexpress sale generated", blank=True)


    

    

    # def get_absolute_url(self):
    #     return reverse("product:product-detail", kwargs={"slug": self.slug})
    
    def get_absolute_url(self):
        return reverse("content:course-detail", kwargs={"slug": self.slug})
    
    def get_update_url(self):
        return reverse("staff:product-update", kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse("staff:product-delete", kwargs={'pk': self.pk})


    @property
    def imageURL(self):
        try:
            url = self.image_store.url
        except:
            url = ''
        print('URL:', url)
        return url

    def __str__(self):
        return f'{self.name_of_product} (${self.aliexpress_price})' 
    

    def save(self, *args, **kwargs):
         
        self.price_margin = self.shopify_price - self.aliexpress_price 

        self.aliexpress_total_sale = self.aliexpress_order * self.shopify_price

        super().save(*args, **kwargs)

    def img_preview(self): #new
        return mark_safe(f'<img src = "{self.product_thumbnail.url}" width = "50"/>')
        
    img_preview.short_description = 'Product Image'
    img_preview.allow_tags = True


class Order(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE),
    start_date = models.DateTimeField(_('start_date'), auto_now_add=True),
    
   
    def __str__(self):
        return self.reference_number

    @property
    def reference_number(self):
        return f"ORDER-{self.pk}"

    def get_raw_subtotal(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_raw_total_item_price()
        return total

    def get_subtotal(self):
        subtotal = self.get_raw_subtotal()
        return "{:.2f}".format(subtotal / 100)

    def get_raw_total(self):
        subtotal = self.get_raw_subtotal()
        # add tax, add delivery, subtract discounts
        # total = subtotal - discounts + tax + delivery
        return subtotal

    def get_total(self):
        total = self.get_raw_total()
        return "{:.2f}".format(total / 100)

class OrderItem(models.Model):
    
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateField(default=timezone.now)
    updated_at = AutoDateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.quantity} x {self.course.name_of_product}"

    # def get_raw_total_item_price(self):
    #     return self.quantity * self.product.price

    # def get_total_item_price(self):
    #     price = self.get_raw_total_item_price()  # 1000
    #     return "{:.2f}".format(price / 100)


class Sale(models.Model):

    course = models.ForeignKey(Course, on_delete=models.CASCADE),
    total_number_of_sale = models.IntegerField(_('total_number_of_sale'), blank=True, null=True, help_text = ""),
    created_at = models.DateField(default=timezone.now),
    updated_at = AutoDateTimeField(default=timezone.now)
    class Meta:
        ordering = [_('-time')]

    def __str__(self):
        return f' ({self.course.name_of_product}), {self.total_number_of_sale}'
    
class Video(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='videos')
    vimeo_id = models.CharField(max_length=50)
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    call_to_action = RichTextUploadingField(blank=True, null=True,)
    description = RichTextUploadingField(blank=True, null=True,)
    order = models.IntegerField(default=1)
    created_at = models.DateField(default=timezone.now)
    updated_at = AutoDateTimeField(default=timezone.now)
    class Meta:
        ordering = ["order"]    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("content:video-detail", kwargs={
            "video_slug": self.slug,
            "slug": self.course.slug
        })


def pre_save_course(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)


def pre_save_video(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)


def post_email_confirmed(request, email_address, *args, **kwargs):
    user = User.objects.get(email=email_address.email)
    free_trial_pricing = Pricing.objects.get(name='Free Trial')
    subscription = Subscription.objects.create(
        user=user, 
        pricing=free_trial_pricing
    )
    stripe_customer = stripe.Customer.create(
        email=user.email
    )
    stripe_subscription = stripe.Subscription.create(
        customer=stripe_customer["id"],
        items=[{'price': 'django-free-trial'}],
        trial_period_days=7
    )
    subscription.status = stripe_subscription["status"]  # trialing
    subscription.stripe_subscription_id = stripe_subscription["id"]
    subscription.save()

email_confirmed.connect(post_email_confirmed)


pre_save.connect(pre_save_course, sender=Course)
# pre_save.connect(pre_save_video, sender=Video)

