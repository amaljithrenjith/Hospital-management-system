from django.contrib import admin
from .models import Booking,Doctors,Department


# Register your models here.
admin.site.register(Booking)
admin.site.register(Doctors)
admin.site.register(Department)
