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
        verbose_name = ("Privacies")
