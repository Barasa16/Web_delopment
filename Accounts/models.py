from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)

    opportunity = models.TextField(max_length=200)
    Company = models.TextField(max_length=200)
    Stage_of_completion = models.TextField(max_length=200)
    Amount = models.DecimalField(max_digits=100, decimal_places=2)

    def __str__(self):
        return f"{self.user.username} Account"

