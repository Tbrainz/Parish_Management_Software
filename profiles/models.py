from django.db import models

# Create your models here.
class ContactModel(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=11)
    email = models.CharField(max_length=50, blank= True, null=True)
    message = models.TextField(max_length= 1000)

    def __str__(self):
        return f"{self.name}"

class MassBookingModel(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=11)
    email = models.CharField(max_length=50, blank= True, null=True)
    thanksgiving = models.CharField(max_length=20, choices=[('YES', 'YES'), ('NO', 'NO')], null=False, blank=False)
    intention = models.TextField(max_length= 1000)

    def __str__(self):
        return f"{self.name}"


class AnnouncementModel(models.Model):
    organization = models.CharField(max_length=100, null=False, blank=False)
    date = models.DateField()
    announcement = models.TextField(max_length=1000)

    def __str__(self):
        return f"{self.organization}"



