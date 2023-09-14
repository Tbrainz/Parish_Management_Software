from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, null=False, blank=True)
    number = models.CharField(max_length=11, null=False, blank=True)
    address = models.CharField(max_length=100, null=False, blank=True)
    marital_status = models.CharField(max_length=100,choices=[('single', 'single'), ('married', 'married'), ('widow', 'widow'), ('widower', 'widower')], null=False, blank=True)
    tribe = models.CharField(max_length=50, null=False, blank=True)
    occupation = models.CharField(max_length=50, null=False, blank=True)
    societies = models.CharField(max_length=100, null=False, blank=True)
    dob = models.DateField(null=False, blank=True)
    image = models.ImageField(upload_to='pics/', null=True)

    def __str__(self):
        return f"{self.full_name}"