from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    summary = models.CharField(max_length=32)
    content = models.TextField()
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Meta:
    permissions = (("project_task", "project task"),)
