from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    deadline = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    # 🔥 IMPORTANT FIX (null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title