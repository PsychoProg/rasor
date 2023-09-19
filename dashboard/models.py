from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
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


class CourseContent(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='contents')
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='course_content/%Y/%m/')
    created_at = models.DateTimeField(auto_now_add=True)
    

class CourseMessage(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="messages")
    sender = models.ForeignKey(USER, on_delete=models.CASCADE)
    content = models.TextField()
    # content = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)


class CoursePracticeFiles(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    uploaded_by = models.ForeignKey(USER, on_delete=models.CASCADE)
    file = models.FileField(upload_to='practice_files/%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True)


class Enrollment(models.Model):
    student = models.ForeignKey(USER, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateTimeField(auto_now_add=True)
