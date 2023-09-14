from django.contrib import admin
from .models import MassBookingModel, AnnouncementModel, ContactModel

# Register your models here.

admin.site.register(MassBookingModel)
admin.site.register(AnnouncementModel)
admin.site.register(ContactModel)