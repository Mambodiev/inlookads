from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, post_save
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify
from django.shortcuts import reverse, get_object_or_404
from django.contrib.auth import get_user_model
from allauth.account.signals import email_confirmed
import stripe

# stripe.api_key = settings.STRIPE_SECRET_KEY

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100)    
    class Meta:
        verbose_name_plural = "Categories"
    def __str__(self):
        return self.name


class Pricing(models.Model):
    name = models.CharField(max_length=100)  # Basic / Pro / Premium

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ("Price")

class Subscription(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pricing = models.ForeignKey(Pricing, on_delete=models.CASCADE, related_name='subscriptions')
    created = models.DateTimeField(auto_now_add=True)
    stripe_subscription_id = models.CharField(max_length=50)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.user.email


# class Course(models.Model):
#     pricing_tiers = models.ManyToManyField(Pricing, blank=True)
#     name = models.CharField(max_length=100)
#     slug = models.SlugField(unique=True)
#     thumbnail = models.ImageField(upload_to="thumbnails/")
#     call_to_action = RichTextUploadingField(blank=True, null=True,)
#     description = RichTextUploadingField(blank=True, null=True,)

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse("content:course-detail", kwargs={"slug": self.slug})

class Store(models.Model):
    name = models.CharField(max_length=100)    

    def __str__(self):
        return self.name
 

class Technology(models.Model):
    name = models.CharField(max_length=100)    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = ("Technologies")


class Country(models.Model):
    name = models.CharField(max_length=100)    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = ("Countries")


class Language(models.Model):
    name = models.CharField(max_length=100)    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = ("Languages")


class Button(models.Model):
    name = models.CharField(max_length=100)    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = ("Buttons")

class Course(models.Model):
    
    name_of_store = models.ForeignKey(Store, related_name='store_name', blank=True, null=True, on_delete=models.CASCADE)
    shopify_links = models.CharField(blank=True, null=True, max_length=500, help_text = "A link that will take to a single the store")
    name_of_product = models.CharField(max_length=100)
    shopify_price = models.IntegerField(default=0,blank=True, null=True, help_text = "Product price from shopify")
    product_thumbnail = models.ImageField(upload_to="thumbnails/", default='products/defaut_image_store_light_blue_bag.jpg')
    store_logo = models.ImageField(upload_to="image_store/",default='products/defaut_image_store.png',
        blank=True)
    aliexpress_order = models.IntegerField(default=0, help_text = "Amount of aliexpress order generated")
    aliexpress_total_sale = models.IntegerField(default=0, help_text = "Amount of aliexpress sale generated")
    aliexpress_price = models.IntegerField(default=0, help_text = "Product price from aliexpress")
    categories = models.ManyToManyField(Category)
    likes = models.IntegerField(default=0, help_text = "Amount of likes generated") 
    comment = models.IntegerField(default=0, help_text = "Amount of comment generated")
    views = models.IntegerField(default=0, help_text = "Amount of views generated")
    links_to_ads = RichTextUploadingField(blank=True, null=True,  help_text = "A link that will take to ads")
    text_that_comes_with_ads = RichTextUploadingField(blank=True, null=True)
    number_of_store_selling = models.IntegerField(default=0, help_text = "Amount of store selling the product")
    number_of_suppliers_selling= models.IntegerField(default=0, help_text = "Amount of suppliers selling the product")
    ads_run_since = models.DateTimeField(auto_now_add=False)
    countries = models.ManyToManyField(Country, max_length=100,)
    technologies =  models.ManyToManyField(Technology)
    languages = models.ManyToManyField(Language)
    buttons = models.ManyToManyField(Button)
    links_to_others_stores = RichTextUploadingField(blank=True, null=True,help_text = "A link that will take to the store", )
    links_to_others_suppliers = RichTextUploadingField(blank=True, null=True,)
    is_faceBook = models.BooleanField(default=False)
    is_pinterest = models.BooleanField(default=False)
    is_tiktok = models.BooleanField(default=False)
    has_video = models.BooleanField(default=False)
    has_photo = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)
    price_margin = models.IntegerField(default=0,blank=True, null=True, help_text = "Profit you get from this product")
    date_we_found = models.DateTimeField(auto_now_add=True)


    

    # def get_absolute_url(self):
    #     return reverse("product:product-detail", kwargs={"slug": self.slug})
    
    def get_absolute_url(self):
        return reverse("content:course-detail", kwargs={"slug": self.slug})
    
    def get_margin(self):
        return "{:.2f}".format(self.price_margin / 100)

    def get_aliexpres(self):
        return "{:.2f}".format(self.aliexpress_price / 100)

    def get_shopify(self):
        return "{:.2f}".format(self.shopify_price / 100)

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
        aliexpress_price = self.shopify_price
        shopify_price = self.aliexpress_price
        if self.shopify_price:
            diff = aliexpress_price - shopify_price
            self.price_margin = round(diff, 2)
        
        super().save(*args, **kwargs)


class OrderItem(models.Model):
    order = models.ForeignKey(
        "Order", related_name='items', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
 
    def __str__(self):
        return f"{self.quantity} x {self.course.name_of_product}"

    # def get_raw_total_item_price(self):
    #     return self.quantity * self.product.price

    # def get_total_item_price(self):
    #     price = self.get_raw_total_item_price()  # 1000
    #     return "{:.2f}".format(price / 100)


class Order(models.Model):
    user = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField(blank=True, null=True)
    ordered = models.BooleanField(default=False)
    
   
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


class Sale(models.Model):


    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # month_name = models.CharField(max_length=50)
    total_number_of_sale = models.IntegerField(blank=True, null=True, help_text = "")
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-time']

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
pre_save.connect(pre_save_video, sender=Video)

