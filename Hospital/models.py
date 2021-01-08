from django.db import models
# Create your models here.
from django.urls import reverse


class Login(models.Model):
    date = models.DateTimeField()
    User_name = models.CharField(max_length=200)
    Password = models.CharField(max_length=200)
    content = models.TextField()


class Doctor(models.Model):
    name = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)

    status = models.BooleanField(default=True)

    speciality = models.CharField(max_length=200, choices=[
        ("cardiologist", "Cardiologist"),
        ("dermatologist", "Dermatologist"),
        ("emergency medecine specialist", "Emergency Medecine Specialists"),
        ("allergist", "Allergists"),
        ("anesthesiologist", "Anesthesiologist"),

    ])

    def get_name(self):
        return self.name + " " + self.first_name

    def __str__(self):
        return "{} ({})".format(self.user_name, self.speciality)


class PatientModel(models.Model):
    name = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    symptom = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)

    status = models.BooleanField(default=True)

    admit_to = models.CharField(max_length=200, choices=[
        ("cardiologist", "Cardiologist"),
        ("dermatologist", "Dermatologist"),
        ("emergency medecine specialist", "Emergency Medecine Specialists"),
        ("allergist", "Allergists"),
        ("anesthesiologist", "Anesthesiologist"),

    ])
    added_date = models.DateTimeField(auto_now=True)

    # recently added
    doctor_id = models.PositiveIntegerField(null=True)
    doctor_name = models.CharField(max_length=200, null=True)

    discharge = models.BooleanField(default=False)

    def get_name(self):
        return self.name + " " + self.first_name

    def __str__(self):
        return "{} ({})".format(self.name, self.symptom)


class Appointment(models.Model):
    description = models.TextField(max_length=500)
    patient_id = models.PositiveIntegerField(null=True)
    doctor_id = models.PositiveIntegerField(null=True)
    date = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    # this is is for storing the name of the doctor  and the patient
    patient_name = models.CharField(max_length=200, null=True)
    doctor_name = models.CharField(max_length=200, null=True)


class Item(models.Model):
    room_charge = models.IntegerField()
    doctor_fee = models.IntegerField()
    medecine_cost = models.IntegerField()
    Other_charge = models.IntegerField()
    patient_id = models.PositiveIntegerField()








