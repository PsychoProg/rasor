from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from decimal import Decimal
from PIL import Image
from dashboard.models import Course
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
    is_validate = models.BooleanField(default=False)
    

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


# class Student(models.Model):
#     student = models.OneToOneField(USER, on_delete=models.CASCADE, related_name='students')
#     courses = models.ManyToManyField(Course)

#     def __str__(self):
#         return self.student.get_full_name

#     def get_absolute_url(self):
#         return reverse("dashboard:profile", kwargs={"pk": self.pk})

#     def delete(self, *args, **kwargs):
#         self.student.delete()
#         super().delete(*args, **kwargs)



# class DepartmentHead(models.Model):
#     pass

# class Artisan(models.Model):
#     pass

# class Mentor(models.Model):
#     pass