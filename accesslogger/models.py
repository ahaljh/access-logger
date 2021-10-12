from django.db import models

# Create your models here.
class AccessLog(models.Model):
    page = models.CharField(max_length=50, help_text='접속한 페이지')
    ip = models.CharField(max_length=30, null=True, blank=True)
    user_agent = models.CharField(max_length=200, null=True, blank=True)
    accessed_time = models.DateTimeField(auto_now_add=True)
