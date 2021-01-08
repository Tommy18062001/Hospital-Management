from django.contrib.auth.models import User
from django.shortcuts import render, redirect, reverse

from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from django.utils import timezone

from .models import Doctor, PatientModel, Appointment, Item

from .forms import DoctorForm, PatientForm, ItemForm, AppointmentForm, DoctorUserForm, PatientUserForm

from django.shortcuts import get_object_or_404

from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, "Hospital/index.html", {})


@ login_required(login_url="login")
def admin_home(request):
    all_doctor = Doctor.objects.all()
    num_doctor = Doctor.objects.all().count()

    all_patient = PatientModel.objects.all()
    num_patient = PatientModel.objects.all().count()

    # all_appointment = Appointment.objects.all()
    num_appointment = Appointment.objects.all().count()

    context = {"num_doctor": num_doctor,
               "all_doctor": all_doctor,
               "all_patient": all_patient,
               "num_patient": num_patient,
               # "all_appointment": all_appointment,
               "num_appointment": num_appointment,

               }

    return render(request, "Hospital/admin_home.html", context)


"""  ------------------------------------------Doctor---------------------------------------------  """


@ login_required(login_url="login")
def admin_home_doctor(request):
    return render(request, "Hospital/admin_home_doctor.html", {})


@ login_required(login_url="login")
def admin_view_doctor(request):
    all = Doctor.objects.all().filter(status=True)
    return render(request, "Hospital/admin_view_doctor.html", {"all": all})


@ login_required(login_url="login")
def admin_view_approval(request):
    to_approve = Doctor.objects.all().filter(status=False)
    return render(request, "Hospital/admin_view_approval.html", {"doctor": to_approve})


@ login_required(login_url="login")
def admin_view_appointment_approval(request):
    to_approve = Appointment.objects.all().filter(status=False)
    return render(request, "Hospital/admin_view_appointment_approval.html", {"appointment": to_approve})


@ login_required(login_url="login")
def approve_appointment(request, my_id):
    obj = Appointment.objects.get(id=my_id)

    # let's accept this doctor but putting his status into True.
    obj.status = True

    # never forget to save it
    obj.save()

    return redirect("admin_view_appointment")


@ login_required(login_url="login")
def reject_appointment(request, my_id):
    obj = Appointment.objects.get(id=my_id)

    obj.delete()

    return redirect("admin_view_appointment_approval")


@ login_required(login_url="login")
def approve_doctor(request, my_id):
    obj = Doctor.objects.get(id=my_id)

    # let's accept this doctor but putting his status into True.
    obj.status = True

    # never forget to save it
    obj.save()

    return redirect("admin_view_doctor")


@ login_required(login_url="login")
def reject_doctor(request, my_id):
    obj = Doctor.objects.get(id=my_id)

    obj.delete()

    return redirect("admin_view_approval")


@ login_required(login_url="login")
def admin_add_doctor(request):
    form = DoctorUserForm()

    if request.method == "POST":
        form = DoctorUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()

            # let's give the user a cue that the account was really created
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            password = form.cleaned_data.get('password')
            mobile = form.cleaned_data.get('mobile')
            address = form.cleaned_data.get('address')
            speciality = form.cleaned_data.get("speciality")

            Doctor.objects.create(
                name=last_name,
                user_name=username,
                first_name=first_name,
                address=address,
                password=password,
                mobile=mobile,
                status=True,
                speciality=speciality
            )

            return redirect('admin_view_doctor')

    return render(request, "Hospital/admin_add_doctor.html", {"form": form})


@ login_required(login_url="login")
def update_doctor(request, my_id):
    doctor = Doctor.objects.get(id=my_id)
    obj = User.objects.all().get(username=doctor.user_name)

    form = DoctorUserForm(request.POST or None, instance=obj)

    if form.is_valid():
        user = form.save()
        user.set_password(user.password)
        user.save()

        # let's give the user a cue that the account was really created
        doctor.user_name = form.cleaned_data.get('username')
        doctor.first_name = form.cleaned_data.get('first_name')
        doctor.name = form.cleaned_data.get('last_name')
        doctor.password = form.cleaned_data.get('password')
        doctor.mobile = form.cleaned_data.get('mobile')
        doctor.address = form.cleaned_data.get('address')
        doctor.symptom = form.cleaned_data.get("symptom")
        doctor.save()

        return redirect('admin_view_doctor')

    return render(request, "Hospital/admin_add_doctor.html", {"form": form})


@ login_required(login_url="login")
def delete_doctor(request, my_id):
    obj = Doctor.objects.all().get(id=my_id)
    obj.delete()
    return redirect("admin_view_doctor")


@ login_required(login_url="login")
def admin_doctor_specialisation(request):
    # i don't know how to add space, so i am going just to create a space as an object
    space = " "

    all = Doctor.objects.all()
    return render(request, "Hospital/admin_doctor_specialisation.html", {"all": all, "space": space} )


"""  ------------------------------------------Patient---------------------------------------------  """


@ login_required(login_url="login")
def admin_home_patient(request):
    return render(request, "Hospital/admin_home_patient.html", {})


@ login_required(login_url="login")
def admin_view_patient(request):
    patients = PatientModel.objects.all()
    return render(request, "Hospital/admin_view_patient.html", {"patients": patients})


@ login_required(login_url="login")
def admin_add_patient(request):
    form = PatientUserForm()

    if request.method == "POST":
        form = PatientUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.doctor_id = request.POST.get("doctor_id")
            user.doctor_name = Doctor.objects.get(id=request.POST.get('doctor_id')).user_name
            user.save()

            # let's give the user a cue that the account was really created
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            password = form.cleaned_data.get('password')
            mobile = form.cleaned_data.get('mobile')
            address = form.cleaned_data.get('address')
            symptom = form.cleaned_data.get("symptom")

            PatientModel.objects.create(
                name=last_name,
                user_name=username,
                first_name=first_name,
                address=address,
                symptom=symptom,
                password=password,
                mobile=mobile,
                status=True,
                doctor_name=user.doctor_name,
            )
            return redirect("admin_view_patient")

    return render(request, "Hospital/admin_add_patient.html", {"form": form})


@ login_required(login_url="login")
def update_patient(request, my_id):
    patient = get_object_or_404(PatientModel, id=my_id)
    obj = User.objects.all().get(username=patient.user_name)

    form = PatientUserForm(request.POST or None, instance=obj)

    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(user.password)
        user.doctor_id = request.POST.get("doctor_id")
        user.doctor_name = Doctor.objects.get(id=request.POST.get('doctor_id')).user_name
        user.save()

        # let's give the user a cue that the account was really created
        patient.user_name = form.cleaned_data.get('username')
        patient.first_name = form.cleaned_data.get('first_name')
        patient.name = form.cleaned_data.get('last_name')
        patient.password = form.cleaned_data.get('password')
        patient.mobile = form.cleaned_data.get('mobile')
        patient.address = form.cleaned_data.get('address')
        patient.symptom = form.cleaned_data.get("symptom")
        patient.doctor_name = user.doctor_name
        patient.save()

        return redirect("admin_view_patient")

    return render(request, "Hospital/admin_add_patient.html", {"form": form})


@ login_required(login_url="login")
def delete_patient(request, my_id):
    obj = PatientModel.objects.all().get(id=my_id)
    obj.delete()
    return redirect("admin_view_patient")


@ login_required(login_url="login")
def admin_discharge_patient(request):
    all = PatientModel.objects.all().filter(discharge=False)
    return render(request, "Hospital/admin_discharge_patient.html", {"all": all})


# this is just for making the number more cool
def number_form(num):
    our_num = list(str(num))

    times = int(len(our_num) / 3)

    for s in range(times):
        id = (-3 * (s + 1)) - s

        our_num.insert(id, " ")

    return "".join(our_num)


@ login_required(login_url="login")
def patient_discharge(request, my_id):
    patient = get_object_or_404(PatientModel, id=my_id)

    patient_date = patient.added_date.date()
    today_date = timezone.now().date()

    day_spent = today_date.day - patient_date.day

    doctor = patient.doctor_name

    form = ItemForm()

    # after discharing the patient, we need to notify that with our status. i mean turn it into false (just as a sign)
    patient.discharge = True
    patient.save()

    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.patient_id = my_id
            item.save()

            room_charge = item.room_charge
            doctor_fee = item.doctor_fee
            medecine_cost = item.medecine_cost
            Other_charge = item.Other_charge

            total = room_charge + doctor_fee + medecine_cost + Other_charge

            return render(request, "Hospital/patient_discharge_bill.html", {
                "patient": patient,
                "doctor_name": doctor,
                "today": today_date,
                "day_spent": day_spent,
                "room_charge": number_form(room_charge),
                "doctor_fee": number_form(doctor_fee),
                "medecine_cost": number_form(medecine_cost),
                "Other_charge": number_form(Other_charge),
                "total": number_form(total)
            })

    return render(request, "Hospital/patient_discharge.html", {
        "patient": patient,
        "doctor_name": doctor,
        "today": today_date,
        "day_spent": day_spent,
        "form": form
    })


"""  ------------------------------------------Appointment---------------------------------------------  """


@ login_required(login_url="login")
def admin_home_appointment(request):
    return render(request, "Hospital/admin_home_appointment.html", {})


@ login_required(login_url="login")
def admin_view_appointment(request):
    appointments = Appointment.objects.all()
    return render(request, "Hospital/admin_view_appointment.html", {"appointments": appointments})


@ login_required(login_url="login")
def admin_book_appointment(request):
    form = AppointmentForm()

    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.doctor_id = request.POST.get('doctor_id')
            appointment.patientId = request.POST.get('patient_id')
            appointment.doctor_name = Doctor.objects.get(id=request.POST.get('doctor_id')).user_name
            appointment.patient_name = PatientModel.objects.get(id=request.POST.get('patient_id')).name
            appointment.status = True
            appointment.save()

            return redirect("admin_view_appointment")

    return render(request, "Hospital/admin_book_appointment.html", {"form": form})


"""  ------------------------------------------Doctor---------------------------------------------  """


@ login_required(login_url="doctor_login")
def doctor_home(request):
    num_patient = PatientModel.objects.all().filter(status=True, doctor_name=request.user).count()
    num_appointment = Appointment.objects.all().filter(status=True, doctor_name=request.user).count()
    num_discharge = PatientModel.objects.all().filter(status=False, doctor_name=request.user).count()

    # all patient in his charge (either permanent or discharged)
    all_appointment = Appointment.objects.all().filter(doctor_name=request.user)

    return render(request, "Hospital/doctor_home.html", {"num_patient": num_patient,
                                                         "num_appointment": num_appointment,
                                                         "num_patient_discharged": num_discharge,
                                                         "all_appointment": all_appointment
                                                         })


# Create your views here.


@ csrf_exempt
def doctor_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if is_doctor(user):
            if user is not None:
                obj = Doctor.objects.all().get(user_name=user)
                if obj.status:
                    login(request, user=user)
                    return redirect("doctor_home")
                else:
                    login(request, user=user)
                    return render(request, "Hospital/doctor_wait_approval.html", {})
        return render(request, "DoctorAccount/login_page.html", {})

    return render(request, "DoctorAccount/login_page.html", {})


@ csrf_exempt
def doctor_register(request):
    form = DoctorUserForm()

    if request.method == "POST":
        form = DoctorUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()

            # let's give the user a cue that the account was really created
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            password = form.cleaned_data.get('password')
            mobile = form.cleaned_data.get('mobile')
            address = form.cleaned_data.get('address')
            speciality = form.cleaned_data.get("speciality")

            Doctor.objects.create(
                name=last_name,
                user_name=username,
                first_name=first_name,
                address=address,
                password=password,
                mobile=mobile,
                status=False,
                speciality=speciality
            )

            messages.info(request, "The account was created successfully for " + username)

            return redirect('doctor_login')

    return render(request, "DoctorAccount/register_page.html", {"form": form})


@ login_required(login_url="doctor_login")
@ csrf_exempt
def doctor_logout(request):
    logout(request)
    return redirect("home")


@ login_required(login_url="doctor_login")
def doctor_patient(request):
    return render(request, "Hospital/doctor_patient.html", {})


@ login_required(login_url="doctor_login")
def doctor_appointment(request):
    return render(request, "Hospital/doctor_appointment.html", {})


@ login_required(login_url="doctor_login")
def doctor_view_patient(request):
    patients = PatientModel.objects.all().filter(status=True, doctor_name=request.user)

    return render(request, "Hospital/doctor_view_patient.html", {"patients": patients})


@ login_required(login_url="doctor_login")
def doctor_view_appointment(request):
    all_appointment = Appointment.objects.all().filter(status=True, doctor_name=request.user)
    patient = PatientModel.objects.all().filter(doctor_name=request.user)

    return render(request, "Hospital/doctor_view_appointment.html", {"appointments": all_appointment,
                                                                     "patient": patient,
                                                                     })


@ login_required(login_url="doctor_login")
def doctor_delete_view_appointment(request):
    all_appointment = Appointment.objects.all().filter(status=True, doctor_name=request.user)

    return render(request, "Hospital/doctor_delete_view_appointment.html", {"appointments": all_appointment,
                                                                     })


@ login_required(login_url="doctor_login")
def doctor_delete_appointment(request, my_id):
    delete_obj = Appointment.objects.all().get(id=my_id)

    # i am not going to delete it literally, i just need to change its status to False.
    delete_obj.status = False
    delete_obj.save()
    return redirect("doctor_delete_view_appointment")


@ login_required(login_url="doctor_login")
# unlike with the admin view, the doctor can only see the details
def doctor_discharge_patient(request):
    patient_discharged = PatientModel.objects.all().filter(status=False, doctor_name=request.user)
    return render(request, "Hospital/doctor_discharge_patient.html", {"patient_discharged": patient_discharged})


"""  ------------------------------------------Patient---------------------------------------------  """


@ login_required(login_url="patient_login")
def patient_home(request):
    # the nearest things we have is the name of the patient.
    # so this is why i use this instead of looking for id or something else

    patient = PatientModel.objects.all().get(name=request.user)

    doctor = Doctor.objects.all().get(user_name=patient.doctor_name)

    return render(request, "Hospital/patient_home.html", {"patient": patient,
                                                          "doctor": doctor})


@ login_required(login_url="patient_login")
def patient_appointment(request):
    return render(request, "Hospital/patient_appointment.html", {})


@ login_required(login_url="patient_login")
def patient_view_appointment(request):
    all_appointment = Appointment.objects.all().filter(patient_name=request.user)
    all_patient = PatientModel.objects.all().filter(name=request.user)

    return render(request, "Hospital/patient_view_appointment.html", {"appointments": all_appointment,
                                                                      "patients": all_patient,
                                                                     })


@ login_required(login_url="patient_login")
def patient_view_discharge(request):
    patient = PatientModel.objects.all().get(name=request.user)

    if patient.discharge:

        patient_date = patient.added_date.date()
        today_date = timezone.now().date()
        day_spent = today_date.day - patient_date.day
        doctor = patient.doctor_name

        item = Item.objects.all().get(patient_id=patient.id)
        room_charge = item.room_charge
        doctor_fee = item.doctor_fee
        medecine_cost = item.medecine_cost
        Other_charge = item.Other_charge

        total = room_charge + doctor_fee + medecine_cost + Other_charge

        return render(request, "Hospital/patient_view_discharge.html", {
            "patient": patient,
            "doctor_name": doctor,
            "today": today_date,
            "day_spent": day_spent,
            "room_charge": number_form(room_charge),
            "doctor_fee": number_form(doctor_fee),
            "medecine_cost": number_form(medecine_cost),
            "Other_charge": number_form(Other_charge),
            "total": number_form(total)
        })

    return render(request, "Hospital/patient_view_discharge_message.html", {})


@ csrf_exempt
def patient_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if is_patient(user):
            if user is not None:
                obj = PatientModel.objects.all().get(user_name=user)
                if obj.status:
                    login(request, user=user)
                    return redirect("patient_home")
                else:
                    login(request, user=user)
                    return render(request, "Hospital/patient_wait_approval.html", {})
        return render(request, "PatientAccount/login_page.html", {})

        # we don't need to store this information, django offer us a login function
    return render(request, "PatientAccount/login_page.html", {})


@ csrf_exempt
def patient_register(request):
    form = PatientUserForm()

    if request.method == "POST":
        form = PatientUserForm(request.POST)
        if form.is_valid():
            print("valid")
            user = form.save()
            user.set_password(user.password)
            user.doctor_id = request.POST.get("doctor_id")
            user.doctor_name = Doctor.objects.get(id=request.POST.get('doctor_id')).user_name
            user.save()

            # let's give the user a cue that the account was really created
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            password = form.cleaned_data.get('password')
            mobile = form.cleaned_data.get('mobile')
            address = form.cleaned_data.get('address')
            symptom = form.cleaned_data.get("symptom")

            PatientModel.objects.create(
                name=last_name,
                user_name=username,
                first_name=first_name,
                address=address,
                symptom=symptom,
                password=password,
                mobile=mobile,
                status=False,
                doctor_name=user.doctor_name
            )

            messages.info(request, "The account was created successfully for " + username)

            return redirect('patient_login')

    return render(request, "PatientAccount/register_page.html", {"form": form})


@ login_required(login_url="patient_login")
@ csrf_exempt
def patient_logout(request):
    logout(request)
    return redirect("home")


@ login_required(login_url="patient_login")
def patient_view_approval(request):
    to_approve = PatientModel.objects.all().filter(status=False)
    return render(request, "Hospital/patient_view_approval.html", {"patient": to_approve})


@ login_required(login_url="patient_login")
def approve_patient(request, my_id):
    obj = PatientModel.objects.get(id=my_id)

    # let's accept this doctor but putting his status into True.
    obj.status = True

    # never forget to save it
    obj.save()

    return redirect("admin_view_patient")


@ login_required(login_url="patient_login")
def reject_patient(request, my_id):
    obj = PatientModel.objects.get(id=my_id)
    obj.delete()

    return redirect("admin_view_approval")


@ login_required(login_url="patient_login")
def patient_book_appointment(request):
    form = AppointmentForm()

    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.doctor_id = request.POST.get('doctor_id')
            appointment.patientId = request.POST.get('patient_id')
            appointment.doctor_name = Doctor.objects.get(id=request.POST.get('doctor_id')).name
            appointment.patient_name = PatientModel.objects.get(id=request.POST.get('patient_id')).name
            appointment.status = False
            appointment.save()

            return redirect("patient_view_appointment")

    return render(request, "Hospital/patient_book_appointment.html", {"form": form})


# last thing i want to do is to create something to differ Doctor, Patient, Admin account
# this method is specifically for my code.

# the admin part is in the account app

def is_patient(the_user):
    patient = PatientModel.objects.all().filter(user_name=the_user)
    return patient.exists()


def is_doctor(the_user):
    doctor = Doctor.objects.all().filter(user_name=the_user)
    return doctor.exists()


"-----------------------------------@TommySylver------------------------------------"
