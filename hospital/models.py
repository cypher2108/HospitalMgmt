from django.db import models


# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.ImageField()
    specialization = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Patient(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    mobile = models.ImageField(null=True)
    age = models.CharField(max_length=5)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=10)

    def __str__(self):
        return self.doctor.name + "  " + self.patient.name

