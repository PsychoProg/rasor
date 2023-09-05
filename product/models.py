from django.db import models
from django.db.models.query import QuerySet
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _ 
from django.utils.text import slugify
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from PIL import Image

USER = get_user_model()

class CustomManager(models.Manager):
    """ Return only published items """
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(status='PB')
    

class Product(models.Model):
    title = models.CharField(max_length=255)
    # author = models.ForeignKey(USER, on_delete=models.CASCADE, related_name='products')
    slug = models.SlugField()
    tags = TaggableManager()
    image = models.ImageField(upload_to='product/%Y/%m/%d')
    content = RichTextField()
    # thumbnail = models.ImageField(upload_to='product/%Y/%m/%d')
    published_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # discuss about prodcut price 

    class Status(models.TextChoices):
        DRAFT = 'DF', _('Draft')
        PUBLISHED = 'PB', _('Published')

    status = models.CharField(choices=Status.choices, default=Status.DRAFT, max_length=2)

    objects = models.Manager()
    published = CustomManager()

    def __str__(self):
        return self.title
    
    class Meta:
        ordering=['-updated_at']
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'
        
    def get_absolute_url(self):
        return reverse('product:products_detail', kwargs={'pk': self.id, 'slug': self.slug })

    def save(self, *args, **kwargs):
        # create seo friendly url by slugify
        self.slug = slugify(self.title)
        # save the profile first
        super().save(*args, **kwargs)
        # resize the thumbnail
        # img = Image.open(self.image.path)
        # if img.height > 555 or img.width > 500:
        #     output_size = (555, 500)
        #     # create a thumbnail
        #     img.thumbnail(output_size)
        #     # overwrite the larger image
        #     img.save(self.image.path)    