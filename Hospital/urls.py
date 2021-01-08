from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("admin/", views.admin_home, name="admin_home"),
    path("admin/Doctor", views.admin_home_doctor, name="admin_home_doctor"),
    path("admin/admin_view_doctor", views.admin_view_doctor, name="admin_view_doctor"),
    path("admin/admin_view_approval", views.admin_view_approval, name="admin_view_approval"),
    path("admin/patient_view_approval", views.patient_view_approval, name="patient_view_approval"),
    path("admin/approve_doctor/<int:my_id>", views.approve_doctor, name="approve_doctor"),
    path("admin/approve_patient/<int:my_id>", views.approve_patient, name="approve_patient"),
    path("admin/approve_appointment/<int:my_id>", views.approve_appointment, name="approve_appointment"),
    path("admin/reject_doctor/<int:my_id>", views.reject_doctor, name="reject_doctor"),
    path("admin/reject_patient/<int:my_id>", views.reject_patient, name="reject_patient"),
    path("admin/reject_appointment/<int:my_id>", views.reject_appointment, name="reject_appointment"),
    path("admin/admin_doctor_specialisation", views.admin_doctor_specialisation, name="admin_doctor_specialisation"),
    path("admin/admin_add_doctor", views.admin_add_doctor, name="admin_add_doctor"),
    path("doctor/update/<int:my_id>", views.update_doctor, name="update"),
    path("doctor/delete/<int:my_id>", views.delete_doctor, name="delete"),

    path("admin/Patient", views.admin_home_patient, name="admin_home_patient"),
    path("admin/admin_view_patient", views.admin_view_patient, name="admin_view_patient"),
    path("admin/admin_add_patient", views.admin_add_patient, name="admin_add_patient"),
    path("patient/update/<int:my_id>", views.update_patient, name="update_patient"),
    path("patient/delete/<int:my_id>", views.delete_patient, name="delete_patient"),
    path("admin/admin_discharge_patient", views.admin_discharge_patient, name="admin_discharge_patient"),
    path("patient/discharge/<int:my_id>", views.patient_discharge, name="patient_discharge"),

    path("admin/Appointment", views.admin_home_appointment, name="admin_home_appointment"),
    path("admin/admin_view_appointment", views.admin_view_appointment, name="admin_view_appointment"),
    path("admin/admin_book_appointment", views.admin_book_appointment, name="admin_book_appointment"),
    path("admin/admin_view_appointment_approval", views.admin_view_appointment_approval, name="admin_view_appointment_approval"),

    path("doctor/", views.doctor_home, name="doctor_home"),
    path("doctor/login", views.doctor_login, name="doctor_login"),
    path("doctor/register", views.doctor_register, name="doctor_register"),
    path("doctor/logout", views.doctor_logout, name="doctor_logout"),
    path("doctor/Patient", views.doctor_patient, name="doctor_patient"),
    path("doctor/doctor_discharge_patient", views.doctor_discharge_patient, name="doctor_discharge_patient"),
    path("doctor/Appointment", views.doctor_appointment, name="doctor_appointment"),
    path("doctor/doctor_view_patient", views.doctor_view_patient, name="doctor_view_patient"),
    path("doctor/doctor_view_appointment", views.doctor_view_appointment, name="doctor_view_appointment"),
    path("doctor/doctor_delete_view_appointment", views.doctor_delete_view_appointment, name="doctor_delete_view_appointment"),
    path("doctor/delete_appointment/<int:my_id>", views.doctor_delete_appointment, name="doctor_delete_appointment"),

    path("patient/", views.patient_home, name="patient_home"),
    path("patient/Discharge", views.patient_view_discharge, name="patient_view_discharge"),
    path("patient/Appointment", views.patient_appointment, name="patient_appointment"),
    path("doctor/patient_view_appointment", views.patient_view_appointment, name="patient_view_appointment"),
    path("admin/patient_book_appointment", views.patient_book_appointment, name="patient_book_appointment"),
    path("patient/login", views.patient_login, name="patient_login"),
    path("patient/register", views.patient_register, name="patient_register"),
    path("patient/logout", views.patient_logout, name="patient_logout"),

]


