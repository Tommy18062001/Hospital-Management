from django import forms
from .models import Doctor, PatientModel, Appointment, Item
from django.contrib.auth.models import User


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = [
            "name",
            "user_name",
            "first_name",
            "address",
            "password",
            "mobile",
            "speciality"
        ]

        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Name',
                                           'style': 'box-shadow: 3px 3px 4px rgba(0,0,0,0.2); '}),
            "user_name": forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'Username',
                                                'style': 'box-shadow: 3px 3px 4px rgba(0,0,0,0.2); '}),
            "first_name": forms.TextInput(attrs={'class': 'form-control',
                                                 'placeholder': 'First Name',
                                                 'style': 'box-shadow: 3px 3px 4px rgba(0,0,0,0.2); '}),
            "address": forms.TextInput(attrs={'class': 'form-control',
                                              'placeholder': 'Address',
                                              'style': 'box-shadow: 3px 3px 4px rgba(0,0,0,0.2); '}),
            "password": forms.PasswordInput(attrs={'class': 'form-control',
                                                   'placeholder': 'Password',
                                                   'style': 'box-shadow: 3px 3px 4px rgba(0,0,0,0.2);'}),
            "mobile": forms.TextInput(attrs={'class': 'form-control',
                                             'placeholder': 'Mobile',
                                             'style': 'box-shadow: 3px 3px 4px rgba(0,0,0,0.2);'}),
        }


class PatientForm(forms.ModelForm):
    doctor_id = forms.ModelChoiceField(queryset=Doctor.objects.all(), empty_label="Doctor Name and Department",
                                       to_field_name="id")

    class Meta:
        model = PatientModel
        fields = [
            "name",
            "user_name",
            "first_name",
            "address",
            "symptom",
            "password",
            "mobile",
        ]

        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Name',
                                           'style': 'box-shadow: 3px 3px 4px rgba(0,0,0,0.2);'}),
            "user_name": forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'Username',
                                                'style': 'box-shadow: 3px 3px 4px rgba(0,0,0,0.2);'}),
            "first_name": forms.TextInput(attrs={'class': 'form-control',
                                                 'placeholder': 'First Name',
                                                 'style': 'box-shadow: 3px 3px 4px rgba(0,0,0,0.2);'}),
            "address": forms.TextInput(attrs={'class': 'form-control',
                                              'placeholder': 'Address',
                                              'style': 'box-shadow: 3px 3px 4px rgba(0,0,0,0.2);'}),
            "symptom": forms.TextInput(attrs={'class': 'form-control',
                                              'placeholder': 'Symptom',
                                              'style': 'box-shadow: 3px 3px 4px rgba(0,0,0,0.2);'}),
            "password": forms.PasswordInput(attrs={'class': 'form-control',
                                                   'placeholder': 'Password',
                                                   'style': 'box-shadow: 3px 3px 4px rgba(0,0,0,0.2);'}),
            "mobile": forms.TextInput(attrs={'class': 'form-control',
                                             'placeholder': 'Mobile',
                                             'style': 'box-shadow: 3px 3px 4px rgba(0,0,0,0.2);'}),
        }


class AppointmentForm(forms.ModelForm):
    doctor_id = forms.ModelChoiceField(queryset=Doctor.objects.all(), empty_label="Doctor Name and Department", to_field_name="id")
    patient_id = forms.ModelChoiceField(queryset=PatientModel.objects.all(), empty_label="Patient Name and Symptoms", to_field_name="id")

    class Meta:
        model = Appointment
        fields = ['description', 'status']

        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        }


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            "room_charge",
            "doctor_fee",
            "medecine_cost",
            "Other_charge",
        ]


# this is the doctor account
class DoctorUserForm(forms.ModelForm):
    mobile = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                           'placeholder': 'Mobile',
                                                           'style': 'box-shadow: 3px 3px 4px rgba(0,0,0,0.2); '}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                            'placeholder': 'Address',
                                                            'style': 'box-shadow: 3px 3px 4px rgba(0,0,0,0.2); '}))
    speciality = forms.ChoiceField(choices=[
        ("cardiologist", "Cardiologist"),
        ("dermatologist", "Dermatologist"),
        ("emergency medecine specialist", "Emergency Medecine Specialists"),
        ("allergist", "Allergists"),
        ("anesthesiologist", "Anesthesiologist"),

    ])

    class Meta:
        model = User

        # what are the field that i want to get
        fields = [
            "username",
            "first_name",
            "last_name",
            "password",
        ]

        widgets = {
            "first_name": forms.TextInput(attrs={'class': 'form-control',
                                                 'placeholder': 'First name',
                                                 'style': 'box-shadow: 3px 3px 4px rgba(0,0,0,0.2); '}),
            "last_name": forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'Name',
                                                'style': 'box-shadow: 3px 3px 4px rgba(0,0,0,0.2); '}),

            "username": forms.TextInput(attrs={'class': 'form-control',
                                               'placeholder': 'Username',
                                               'style': ' box-shadow: 3px 3px 4px rgba(0,0,0,0.2); '}),
            "password": forms.PasswordInput(attrs={'class': 'form-control',
                                                   'placeholder': 'Password',
                                                   'style': ' box-shadow: 3px 3px 4px rgba(0,0,0,0.2); '}),

        }


class PatientUserForm(forms.ModelForm):
    doctor_id = forms.ModelChoiceField(queryset=Doctor.objects.all(), empty_label="Doctor Name and Department",
                                       to_field_name="id")

    mobile = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                           'placeholder': 'Mobile',
                                                           'style': 'box-shadow: 3px 3px 4px rgba(0,0,0,0.2); '}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                            'placeholder': 'Address',
                                                            'style': 'box-shadow: 3px 3px 4px rgba(0,0,0,0.2); '}))
    symptom = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                            'placeholder': 'Symptom',
                                                            'style': 'box-shadow: 3px 3px 4px rgba(0,0,0,0.2); '}))

    class Meta:
        model = User

        # what are the field that i want to get
        fields = [
            "username",
            "first_name",
            "last_name",
            "password",
        ]

        widgets = {
            "first_name": forms.TextInput(attrs={'class': 'form-control',
                                                 'placeholder': 'First name',
                                                 'style': ' box-shadow: 3px 3px 4px rgba(0,0,0,0.2); '}),
            "last_name": forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'Name',
                                                'style': 'box-shadow: 3px 3px 4px rgba(0,0,0,0.2); '}),

            "username": forms.TextInput(attrs={'class': 'form-control',
                                               'placeholder': 'Username',
                                               'style': 'box-shadow: 3px 3px 4px rgba(0,0,0,0.2); '}),
            "password": forms.PasswordInput(attrs={'class': 'form-control',
                                                   'placeholder': 'Password',
                                                   'style': '; box-shadow: 3px 3px 4px rgba(0,0,0,0.2); '}),

        }



