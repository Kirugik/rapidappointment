from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Doctor, Patient, Appointment

# Create your views here.
def home(request):
    return render(request, 'appointment/home.html') 


def about(request):
    return render(request, 'appointment/about.html') 


def contact(request): 
    return render(request, 'appointment/contact.html') 




def admin_login(request):
    error = ""

    if request.method == 'POST':
        username = request.POST['username'] 
        password = request.POST['password'] 

        user = authenticate(username=username, password=password) 

        try:
            if user.is_staff:
                login(request, user)
                error = "no"
                return redirect('admin-dashboard')  
            else:
                error = "yes"
        except:
            error = "yes"

    context = {'error': error} 
    return render(request, 'auth/login.html', context)  




def admin_dashboard(request):
    if not request.user.is_staff:
        return redirect('admin-login') 

    doctors = Doctor.objects.all() 
    patients = Patient.objects.all()
    appointments = Appointment.objects.all()

    docs = 0;
    pats = 0;
    appoints = 0;

    for doc in doctors:
        docs+=1;

    for patient in patients:
        pats+=1;

    for appointment in appointments:
        appoints+=1;

    context = {'docs': docs, 'pats': pats, 'appoints': appoints}

    return render(request, 'appointment/admin_dashboard.html', context) 




def admin_logout(request):
    if not request.user.is_staff:
        return redirect('admin-login') 
        
    logout(request)
    return redirect('home')  




def add_doctor(request):
    error = ""
    
    if not request.user.is_staff:
        return redirect('admin-login')

    if request.method == 'POST':
        fname = request.POST['first_name'] 
        lname = request.POST['last_name'] 
        gender = request.POST['gender'] 
        department = request.POST['department'] 
        specialty = request.POST['specialty']
        phone = request.POST['phone'] 
        address = request.POST['address'] 

        try:
            Doctor.objects.create(
                first_name = fname, 
                last_name = lname,
                gender = gender,
                department = department,
                specialty = specialty,
                phone = phone, 
                address = address, 
            )
            error = "no"
        
        except:
            error = "yes"

    context = {'error': error} 
    return render(request, 'appointment/add_doctor.html', context) 



def doctors(request):
    if not request.user.is_staff:
        return redirect('admin-login')
    doctors = Doctor.objects.all()

    context = {'doctors': doctors}
    return render(request, 'appointment/doctors.html', context)



def remove_doctor(request, doc_id):
    if not request.user.is_staff:
        return redirect('admin-login')
    docs = Doctor.objects.get(id=doc_id)
    docs.delete()

    return redirect('doctors') 



def add_patient(request):
    error = ""
    
    if not request.user.is_staff:
        return redirect('admin-login')

    if request.method == 'POST':
        fname = request.POST['first_name'] 
        lname = request.POST['last_name'] 
        age = request.POST['age']  
        gender = request.POST['gender']  
        phone = request.POST['phone'] 
        email = request.POST['email']  
        address = request.POST['address'] 

        try:
            Patient.objects.create( 
                first_name = fname,
                last_name = lname,
                age = age,
                gender = gender, 
                phone = phone,
                email = email,
                address = address, 
            )
            error = "no"
        
        except:
            error = "yes"

    context = {'error': error} 
    return render(request, 'appointment/add_patient.html', context) 




def patients(request):
    if not request.user.is_staff:
        return redirect('admin-login')
    patients = Patient.objects.all()

    context = {'patients': patients}
    return render(request, 'appointment/patients.html', context)



def remove_patient(request, patient_id):
    if not request.user.is_staff:
        return redirect('admin-login')
    patient = Patient.objects.get(id=patient_id)
    patient.delete()

    return redirect('patients') 





def request_appointment(request):
    error = ""
    
    # if not request.user.is_staff:
    #     return redirect('admin-login')
    
    doctors = Doctor.objects.all() 
    patients = Patient.objects.all()

    if request.method == 'POST':
        doctor_name = request.POST['doctor_name'] 
        patient_name = request.POST['patient_name'] 
        symptoms = request.POST['symptoms'] 
        date = request.POST['date'] 
        time = request.POST['time'] 
        
        # doctor = Doctor.objects.filter(name=doctor_name).first()
        # patient = Patient.objects.filter(name=patient_name).first()

        try:
            Appointment.objects.create( 
                doctor_name = doctor_name,
                patient_name = patient_name,
                symptoms = symptoms,
                date = date,
                time = time,
            )
            error = "no"  
        
        except:
            error = "yes"

    context = {'doctors': doctors, 'patients': patients, 'error': error} 
    return render(request, 'appointment/request_appointment.html', context) 



def appointments(request):
    if not request.user.is_staff:
        return redirect('admin-login')
    appointments = Appointment.objects.all()

    context = {'appointments': appointments}
    return render(request, 'appointment/appointments.html', context)


def remove_appointment(request, appointment_id):
    if not request.user.is_staff:
        return redirect('admin-login')
    appointment = Appointment.objects.get(id=appointment_id)
    appointment.delete()

    return redirect('appointments') 
    
