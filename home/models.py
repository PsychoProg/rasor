from django.db import models
from django.contrib.auth.models import User
from django.db.models.query import QuerySet 
from django.utils.translation import gettext_lazy as _ 
from ckeditor.fields import RichTextField


class CustomManager(models.Manager):
    """ Return only published items """
    def get_queryset(self) -> QuerySet:
        return super().get_queryset()


class ListBox(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to='home/psot_list/%Y/%m')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Status(models.TextChoices):
        DRAFT = 'DF', _('Draft')
        PUBLISHED = 'PB', _('Published')

    status = models.CharField(choices=Status.choices, default=Status.DRAFT, max_length=2)

    published = CustomManager()
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
    


class News(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='news')
    content = RichTextField()
    image = models.ImageField(upload_to='home/news/%Y/%m')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Status(models.TextChoices):
        DRAFT = 'DF', _('Draft')
        PUBLISHED = 'PB', _('Published')

    status = models.CharField(choices=Status.choices, default=Status.DRAFT, max_length=2)
    
    published = CustomManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
    


