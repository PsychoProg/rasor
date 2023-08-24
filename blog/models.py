from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField
from PIL import Image


class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    tags = TaggableManager()
    image = models.ImageField(null=True, blank=True)
    content = RichTextField()
    thumbnail = models.ImageField(upload_to='product/%Y/%m/%d')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # discuss about prodcut price 

    def __str__(self):
        return self.title
    
    class Meta:
        ordering=['-updated_at']

    def get_absolute_url(self):
        return reverse('blog:products_list', kwargs={'pk': self.pk, 'slug': self.slug })

    def save(self, *args, **kwargs):
        # save the profile first
        super().save(*args, **kwargs)
        # resize the image
        img = Image.open(self.photo.path)
        if img.height > 255 or img.width > 200:
            output_size = (255, 200)
            # create a thumbnail
            img.thumbnail(output_size)
            # overwrite the larger image
            img.save(self.photo.path)    