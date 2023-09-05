from django.db import models
from django.db.models.query import QuerySet
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _ 
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from PIL import Image

USER = get_user_model()

class CustomManager(models.Manager):
    """ Return only published items """
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(status='PB')
    