from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, post_save
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from allauth.account.signals import email_confirmed
import stripe
from  embed_video.fields  import  EmbedVideoField

# stripe.api_key = settings.STRIPE_SECRET_KEY

User = get_user_model()

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


class Course(models.Model):
    option_ads = [
        ('faceBook', 'FaceBook'),
        ('instagram', 'Instagram'),
        ('Tiktok', 'Tiktok'),
    ]
    option_ads_type = [
        ('video', 'Video'),
        ('photo', 'Photo'),
        ('both', 'Both'),
    ]

    gender_options = [
        ('male or Female', 'Male or Female'),
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    option_language = [
        ('english', 'English'),
        ('armenian', 'Armenian'),
        ('belarusian', 'Belarusian'),
        ('bengali', 'Bengali'),
        ('bosnia', 'Bosnia'),
        ('bulgarian', 'Bulgarian'),
        ('bumese', 'Bumese'),
        ('catalan', 'Catalan'),
        ('central Kurdish', 'Central Kurdish'),
        ('croatian', 'Croatian'),
        ('czech', 'Czech'),
        ('danish', 'Danish'),
        ('dutch', 'Dutch'),
        ('estonian', 'Estonian'),
        ('finnish', 'Finnish'),
        ('french', 'French'),
        ('georgian', 'Georgian'),
        ('german', 'German'),
        ('gujarati', 'Gujarati'),
        ('haitian', 'Haitian'),
        ('hebrew', 'Hebrew'),
        ('hindi', 'Hindi'),
        ('hungarian', 'Hungarian'),
        ('indonesian', 'Indonesian'),
        ('italian', 'Italian'),
        ('japanese', 'Japanese'),
        ('javanese', 'Javanese'),
        ('kannada', 'Kannada'),
        ('kazakh', 'Kazakh'),
        ('khmer', 'Khmer'),
        ('korean', 'Korean'),
        ('latvian', 'Latvian'),
        ('lithuanian', 'Lithuanian'),
        ('maithili', 'Maithili'),
        ('malay', 'Malay'),
        ('malayalam', 'Malayalam'),
        ('mandarin Chinese', 'Mandarin Chinese'),
        ('marathi', 'Marathi'),
        ('modern Greek', 'Modern Greek'),
        ('nepali', 'Nepali'),
        ('north Azerbaijani', 'North Azerbaijani'),
        ('northern Uzbek', 'Northern Uzbek'),
        ('norwegian bokmål', 'Norwegian bokmål'),
        ('norwegian Nynorsk', 'Norwegian Nynorsk'),
        ('oriya', 'Oriya'),
        ('persian', 'Persian'),
        ('polish', 'Polish'),
        ('portuguese', 'Portuguese'),
        ('romanian', 'Romanian'),
        ('russian', 'Russian'),
        ('Serbian', 'Serbian'),
        ('slovak', 'Slovak'),
        ('slovenian', 'Slovenian'),
        ('somali', 'Somali'),
        ('spanish', 'Spanish'),
        ('sudanese', 'Sudanese'),
        ('swahili', 'Swahili'),
        ('swedish', 'Swedish'),
        ('tagalog', 'Tagalog'),
        ('tajik', 'Tajik'),
        ('tamil', 'Tamil'),
        ('telugu', 'Telugu'),
        ('thai', 'Thai'),
        ('tibetan', 'Tibetan'),
        ('turkish', 'Turkish'),
        ('turkmen', 'Turkmen'),
        ('uighur', 'Uighur'),
        ('ukrainian', 'Ukrainian'),
        ('urdu', 'Urdu'),
        ('vietnamese', 'Vietnamese'),
    ]
    option_button = [
        ('buy now', 'Buy Now'),
        ('shop now', 'Shop Now'),
        ('learn more', 'Learn More'),
        ('sign up', 'Sign Up'),
        ('send message', 'Send Message'),
        ('book now', 'Book Now'),
        ('install now', 'Install Now'),
        ('get directions', 'Get Directions'),
        ('watch more', 'Watch More'),
        ('view', 'View'),
        ('apply now', 'Apply Now'),
        ('like this page', 'Like This Page'),
        ('download', 'Download'),
        ('get offer', 'Get Offer'),
        ('get tickets', 'Get Tickets'),
        ('play game', 'Play Game'),
        ('try it', 'Try It'),
        ('contact us', 'Contact Us'),
        ('send whatsapp message', 'Send Whatsapp Message'),
        ('get quote', 'Get Quote'),
        ('call now', 'Call Now'),
        ('donate now', 'Donate Now'),
        ('buy tickets', 'Buy Tickets'),
        ('listen now', 'Listen Now'),
        ('subscribe', 'Subscribe'),
        ('get show times', 'Get Show Times'),
        ('view event', 'View Event'),
        ('see menu', 'See Menu'),
        ('read', 'Read'),
        ('use app', 'Use App'),
        ('order now', 'Order Now'),
        ('request time', 'Request Time'),
        ('join', 'Join'),
        ('open link', 'Open Link'),
        ('start order', 'Start Order'),
        ('install app', 'Install App'),
        ('get your code', 'Get Your Code'),
        ('see more', 'See More'),
        ('play now', 'Play Now'),
        ('see details', 'See Details'),
        ('open camera', 'Open Camera'),
        ('sell now', 'Sell Now'),
        ('buy', 'Buy'),
        ('about this website', 'About This Website'),
        ('messsage', 'Messsage'),
        ('follow', 'Follow'),
        ('try it', 'Try it'),
        ('like page', 'Like Page'),
        ('donate', 'Donate'),
        ('watch video', 'Watch Video'),
        ('visit website', 'Visit Website'),
        ('register now', 'Register Now'),
        ('email now', 'Email Now'),
        ('use offer', 'Use Offer'),
        ('add to profil', 'Add To Profil'),
        ('turn on', 'Turn On'),
        ('invite friends', 'Invite Friends'),
        ('see more', 'see more'),
        ('visit instagram profile', 'Visit Instagram Profile'),
        ('go live', 'go live'),
        ('add to cart', 'Add To Cart'),
        ('vote now', 'Vote Now'),
        ('intrested', 'Intrested'),
        ('see all events', 'See All Events'),
        ('save', 'Save'),
        ('search', 'Search'),
        ('remind me', 'Remind Me'),
        ('watch yours', 'Watch Yours'),
        ('save offer', 'Save Offer'),
        ('get deal', 'Get Deal'),
        ('get reminded', 'Get Reminded'),
        ('book test drive', 'Book Test Drive'),
        ('call', 'Call'),
    ]
    country_choices = [
        ('united States', 'United States'),
        ('United Kingdom', 'United Kingdom'),
        ('Canada', 'Canada'),
        ('Australia', 'Australia'),
        ('New Zealand', 'New Zealand'),
        ('Sweden', 'Sweden'),
        ('Denmark', 'Denmark'),
        ('Iceland', 'Iceland'),
        ('Norway', 'Norway'),
        ('Finland', 'Finland'),
        ('The Netherlands', 'The Netherlands'),
        ('Ireland', 'Ireland'),
        ('Germany', 'Germany'),
        ('South Korea', 'South Korea'),
        ('Switzerland', 'Switzerland'),
        ('Belgium', 'Belgium'),
        ('Israel', 'Israel'),
        ('Italy', 'Italy'),
        ('France', 'France'),
        ('Spain', 'Spain'),
        ('Portugal', 'Portugal'),
        ('Austria', 'Austria'),
        ('Hungary', 'Hungary'),
        ('Poland', 'Poland'),
        ('Czech Republic', 'Czech Republic'),
        ('UAE', 'UAE'),
        ('South Africa', 'South Africa'),
        ('The Philippines', 'The Philippines'),
        ('Japan', 'Japan'),
        ('Singapore', 'Singapore'),
        ('Argentina', 'Argentina'),
        ('Mexico', 'Mexico'),
    ]
    technology_options = [
        ('shopify', 'Shopify'),
        ('wooCommerce', 'WooCommerce'),
        ('cart functionality', 'Cart Functionality'),
        ('magento', 'magento'),
        ('salesforce commerce cloud', 'Salesforce Commerce Cloud'),
        ('prestashop', 'PrestaShop'),
        ('vtex', 'VTEX'),
        ('bigcommerce', 'Bigcommerce'),
        ('ibm websphere commerce', 'IBM Websphere Commerce'),
        ('sap commerce cloud', 'SAP Commerce Cloud'),
        ('shopware', 'Shopware'),
        ('shoptet', 'Shoptet'),
        ('opencart', 'OpenCart'),
        ('nopcommerce', 'nopcommerce'),
        ('oracle commerce', 'Oracle Commerce'),
        ('intershop', 'Intershop'),
        ('hybris', 'Hybris'),
        ('zen cart', 'Zen Cart'),
        ('oracle commerce cloud', 'Oracle Commerce Cloud'),
        ('lightspeed ecom', 'Lightspeed eCom'),
        ('epages', 'EPages'),
        ('cloudcart', 'CloudCart'),
        ('kajabi', 'Kajabi'),
        ('loja integrada', 'Loja Integrada'),
        ('oxid eshop', 'OXID eShop'),
        ('riskified', 'Riskified'),
        ('x-cart', 'X-Cart'),
        ('commerce server', 'Commerce Server'),
        ('drupal commerce', 'Drupal Commerce'),
        ('oscommerce', 'osCommerce'),
        ('91app', '91App'),
        ('nuvemshop', 'Nuvemshop'),
        ('mycashflow', 'Mycashflow'),
        ('ticimax', 'Ticimax'),
        ('ecwid', 'Ecwid'),
        ('gambio', 'Gambio'),
        ('craft commerce', 'Craft Commerce'),
        ('ideasoft', 'Ideasoft'),
        ('ceres', 'Ceres'),
        ('t-soft', 'T-Soft'),
        ('storeden', 'Storeden'),
        ('vtex integrated store', 'VTEX Integrated Store'),
        ('ccv shop', 'CCV Shop'),
        ('big cartel', 'Big Cartel'),
        ('miva', 'Miva'),
        ('irroba', 'Irroba'),
        ('volusion', 'Volusion'),
        ('yepcomm', 'Yepcomm'),
        ('xtcommerce', 'xtCommerce'),
        ('ec-cube', 'EC-CUBE'),
    ]
   
    shopify_url = models.CharField(max_length=1100,blank=False, unique=True)
    name = models.CharField(max_length=100)
    # description = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True)
    thumbnail = models.ImageField(upload_to="thumbnails/", default='products/defaut_image_store_light_blue_bag.jpg')
    product_video = EmbedVideoField(blank=True, null=True,)
    image_store = models.ImageField(upload_to="image_store/",default='products/defaut_image_store.png',
        blank=True)
    aliexpress_order = models.IntegerField(default=0, help_text = "Amount of aliexpress order generated")
    number_of_store_selling = models.IntegerField(default=0, help_text = "Amount of store selling the product")
    number_of_suppliers_selling= models.IntegerField(default=0, help_text = "Amount of suppliers selling the product")
    aliexpress_total_sale = models.IntegerField(default=0, help_text = "Amount of aliexpress sale generated")
    likes = models.IntegerField(default=0, help_text = "Amount of likes generated")
    comment = models.IntegerField(default=0, help_text = "Amount of comment generated")
    views = models.IntegerField(default=0, help_text = "Amount of views generated")
    shopify_price = models.IntegerField(default=0,blank=True, null=True, help_text = "Product price from shopify")
    aliexpress_price = models.IntegerField(default=0, help_text = "Product price from aliexpress")
    price_margin = models.IntegerField(default=0,blank=True, null=True, help_text = "Profit you get from this product")
    product_vimeo_id = models.CharField(max_length=50, blank=True, null=True,) 
    last_seen = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=False)
    countries = models.CharField(max_length=100, choices=country_choices, default='United States')
    ads_type = models.CharField(max_length=250, choices=option_ads_type, default='Video')
    media_type = models.CharField(max_length=250, choices=option_ads, default='video')
    gender = models.CharField(max_length=250, choices=gender_options, default='Male or Female')
    technology = models.CharField(max_length=250, choices=technology_options, default='Shopify')
    language= models.CharField(max_length=250, choices=option_language, default='English')
    button = models.CharField(max_length=250, choices=option_button, default='Buy Now')
    store_name = models.CharField(max_length=500, help_text = "store or ads name",  blank=True, null=True,)
    links_to_ads = models.CharField(blank=True, null=True, max_length=500, help_text = "A link that will take to ads")
    links_to_a_single_store = models.CharField(blank=True, null=True, max_length=500, help_text = "A link that will take to a single the store")
    text_that_comes_with_ads = RichTextUploadingField(blank=True, null=True)
    links_to_others_stores = RichTextUploadingField(blank=True, null=True,help_text = "A link that will take to the store", )
    links_to_others_suppliers = RichTextUploadingField(blank=True, null=True,)
    is_faceBook = models.BooleanField(default=True)
    is_pinterest = models.BooleanField(default=False)
    is_tiktok = models.BooleanField(default=False)
    

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
        return f'{self.name} (${self.aliexpress_price})' 
    

    def save(self, *args, **kwargs):
        aliexpress_price = self.shopify_price
        shopify_price = self.aliexpress_price
        if self.shopify_price:
            diff = aliexpress_price - shopify_price
            self.price_margin = round(diff, 2)
        
        super().save(*args, **kwargs)


class Sale(models.Model):


    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # month_name = models.CharField(max_length=50)
    total_number_of_sale = models.IntegerField(blank=True, null=True, help_text = "")
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-time']

    def __str__(self):
        return f' ({self.course.name}), {self.total_number_of_sale}'
    
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