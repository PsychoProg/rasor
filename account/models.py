from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.conf import settings
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.db.models import Q
from PIL import Image
from django.contrib.auth.models import User
USER = get_user_model()


class OtpCode(models.Model):
    user = models.ForeignKey(USER, on_delete=models.CASCADE, related_name='otp_codes')
    created_at = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = 'کد فعال سازی'
        verbose_name_plural = 'کد های فعال سازی'

class ValidateProfile(models.Model):
    class Gender(models.TextChoices):
        MALE = 'MALE', _('male')
        FEMALE = 'FEMALE', _('female')

    class UserRole(models.TextChoices):
        STUDENT = 'STUDENT', _('Student')
        MENTOR = 'MENTOR', _('Mentor')
        ARTISAN = 'ARTISAN', _('Artisan')
        
    user = models.OneToOneField(USER, on_delete=models.CASCADE)
    gender = models.CharField(choices=Gender.choices, default=Gender.MALE)
    validate_image = models.ImageField(upload_to='validation_image/%Y/%m/%d/')
    register_as = models.CharField(choices=UserRole.choices, default=UserRole.STUDENT)    

    def __str__(self):
        return f"{self.user.username}"

    class Meta:
        verbose_name = 'تایید پروفایل'
        verbose_name_plural = 'تایید پروفایل ها'

    @property
    def get_full_name(self):
        full_name = self.username
        if self.first_name and self.last_name:
            full_name = self.first_name + " " + self.last_name
        return full_name

    

class Profile(models.Model):
    class DegreeChoice(models.TextChoices):
        PHD = 'PHD', _('دکتری')
        POSTGRADUATED = 'Postgraduated', _('کارشناسی ارشد')
        UNDERGRADUATED = 'Undergraduated', _('کارشناسی')
        ASSOCIATE_OF_ART = 'Associate_of_art', _('دیپلم کاردانی')
        ASSOCIATE_OF_SCIENCE = 'Associate_of_science', _('دیپلم تجربی')
        ASSOCIATE_OF_MATH = 'Associate_of_math', _('دیپلم ریاضی')
        ASSOCIATE_OF_LIBERAL_ARTS = 'Associate_of_liberal_arts', _('دیپلم انسانی')
        
    user = models.OneToOneField(USER, on_delete=models.CASCADE, related_name='profiles')
    degree = models.CharField(choices=DegreeChoice.choices, default=DegreeChoice.ASSOCIATE_OF_SCIENCE)
    phone = models.CharField(max_length=12)
    image = models.ImageField(upload_to='profile_pictures/%Y/%m/%d/', default='default.png', null=True)
    address = models.CharField(max_length=255)
    # Role
    is_dep_head = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)    
    is_mentor = models.BooleanField(default=False)
    is_artisan = models.BooleanField(default=False)
    profile_done = models.BooleanField(default=False)

    @property
    def get_user_role(self):
        if self.is_dep_head:
            return "DepartmentHead"
        elif self.is_mentor:
            return "Mentor"
        elif self.is_student:
            return "Student"
        elif self.is_artisan:
            return "Artisan"


    def __str__(self):
        if self.user.first_name and self.user.last_name:
            return f"{self.user.first_name} {self.user.last_name} Profile"
        else:
            return f"{self.user.username} Profile"

    def get_picture(self):
        try:
            return self.picture.url
        except:
            no_picture = settings.MEDIA_URL + 'default.png'
            return no_picture

    def get_absolute_url(self):
        return reverse('profile_single', kwargs={'id': self.id})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        try:
            img = Image.open(self.picture.path)
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.picture.path)
        except:
            pass

    def delete(self, *args, **kwargs):
        if self.picture.url != settings.MEDIA_URL + 'default.png':
            self.picture.delete()
        super().delete(*args, **kwargs)

    class Meta:
            verbose_name = 'پروفایل'
            verbose_name_plural = 'پروفایل ها'


class Student(models.Model):
    pass

class DepartmentHead(models.Model):
    pass

class Artisan(models.Model):
    pass

class Mentor(models.Model):
    pass