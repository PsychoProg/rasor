from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
from decimal import Decimal 

USER = get_user_model()

class Comments(models.Model):
    user = models.ForeignKey(USER, on_delete=models.CASCADE, related_name='comments')
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at']),
        ]
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'


class Course(models.Model):
    mentor = models.ForeignKey(USER, on_delete=models.CASCADE, related_name='courses')
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='product/courses/%Y/')
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "دوره"
        verbose_name_plural = "دوره ها"

class CourseRegistered(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='registrations')
    student = models.ForeignKey(USER, on_delete=models.CASCADE, related_name='courses_registered')
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.course.title} {self.student.username}"

    class Meta:
        verbose_name = "ثبت نام"
        verbose_name_plural = "ثبت نام ها"


def validate_file_size(value):
    filesize = value.size
    if filesize > 2 * 1024 * 1024: # 10 MB
        raise ValidationError(_("حجم مجاز فایل تا ۲ مگابایت"))


class CourseContent(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='contents')
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='course_content/%Y/%m/', validators=[
        FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'pdf', 'mp4'], message='فرمت فایل مجاز نیست.'),
        validate_file_size,
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.course.title} {self.title}"

    class Meta:
        ordering = ['created_at']
        verbose_name = "محتوای دوره"
        verbose_name_plural = "محتوای دوره ها"


class CourseMessage(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="messages")
    sender = models.ForeignKey(USER, on_delete=models.CASCADE)
    content = models.TextField()
    # content = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} - {self.course}"

    class Meta:
        ordering = ['created_at']
        verbose_name = "اعلان دوره"
        verbose_name_plural = "اعلان دوره"


# class CoursePracticeFiles(models.Model):
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     title = models.CharField(max_length=255)
#     uploaded_by = models.ForeignKey(USER, on_delete=models.CASCADE)
#     file = models.FileField(upload_to='practice_files/%Y/%m/%d/')
#     created_at = models.DateTimeField(auto_now_add=True)

#     # def __str__(self):
#     #     return self.title 

#     class Meta:
#         ordering = ['created_at']
#         verbose_name = "فایل تمرین"
#         verbose_name_plural = "فایل های تمرین "
