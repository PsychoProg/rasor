from django.db import models
# from django.contrib.auth.models import User
from django.db.models.query import QuerySet 
from django.utils.translation import gettext_lazy as _ 
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField

USER = get_user_model()

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
        verbose_name = 'تصویر صفحه اصلی '
        verbose_name_plural = 'تصاویر صفحه اصلی'


class News(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(USER, on_delete=models.PROTECT, related_name='news')
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
        verbose_name = 'خبر'
        verbose_name_plural = 'اخبار'


class PageContent1(models.Model):
    title = models.CharField(max_length=155, null=True, blank=True)
    author = models.ForeignKey(USER, on_delete=models.PROTECT)
    content = models.TextField()
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'متن صفحه بخش اول'
        verbose_name_plural = 'متن صفحه بخش اول'


class PageContent2(models.Model):
    title = models.CharField(max_length=155, null=True, blank=True)
    content = models.TextField()
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'متن صفحه بخش دوم'
        verbose_name_plural = 'متن صفحه بخش دوم'


class CompanyInfo(models.Model):
    country = models.CharField(max_length=155, null=True, blank=True)
    provience = models.CharField(max_length=155, null=True, blank=True)
    city = models.CharField(max_length=155, null=True, blank=True)
    phone = models.CharField(max_length=13, null=True, blank=True)

    class Meta:
        verbose_name = 'اطلاعات شرکت'
        verbose_name_plural = 'اطلاعات شرکت'

class ShareLinks(models.Model):
    instagram = models.CharField(max_length=255)
    telegram = models.CharField(max_length=255)
    gmail = models.CharField(max_length=255)
    youtube = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'لینک'
        verbose_name_plural = 'لینک ها'


