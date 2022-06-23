from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.home, name='home'), 
    path('about/', views.about, name='about'), 
    path('contact/', views.contact, name='contact'),  

    path('admin-login/', views.admin_login, name='admin-login'),
    path('admin-dashboard/', views.admin_dashboard, name='admin-dashboard'), 
    path('admin-logout/', views.admin_logout, name='admin-logout'),

    path('add-doctor/', views.add_doctor, name='add-doctor'),
    path('doctors/', views.doctors, name='doctors'),
    path('remove-doctor/<int:doc_id>', views.remove_doctor, name='remove-doctor'),

    path('add-patient/', views.add_patient, name='add-patient'),
    path('patients/', views.patients, name='patients'),
    path('remove-patient/<int:patient_id>', views.remove_patient, name='remove-patient'),  

    path('request-appointment/', views.request_appointment, name='request-appointment'), 
    path('appointments/', views.appointments, name='appointments'), 
    path('remove-appointment/<int:appointment_id>', views.remove_appointment, name='remove-appointment'), 
] 