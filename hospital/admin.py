from django.contrib import admin

# Register your models here.
from hospital.models import Doctor, Patient, Appointment

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)
