from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager


class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    tags = TaggableManager()
    description = models.TextField()
    image = models.ImageField(upload_to='product/%Y/%m/%d')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # discuss about prodcut price 

    def __str__(self):
        return self.title
    
    class Meta:
        ordering=['-updated_at']

    def get_absolute_url(self):
        return reverse('product:product_list', kwargs={'pk': self.pk, 'slug': self.slug })
    