from django.db import models
from django.contrib.auth import get_user_model

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