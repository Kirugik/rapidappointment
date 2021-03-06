from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
from .models import Doctor, Patient, Appointment
from django.core.mail import send_mail 

# Create your views here.
def home(request):
    return render(request, 'appointment/home_old.html') 


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




def sign_up(request):
    if request.method== 'POST':
        username=request.POST['username']
        email=request.POST["email"]
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1 != password2:
            messages.error(request,"Passwords Do Not Match!!")
            return redirect('sign-up')
            
        new_user=User.objects.create_user(
            username=username,
            email=email,
            password=password1,
        )
        new_user.save()
        return redirect('sign-in') 

    return render(request, 'auth/sign_up.html') 



def sign_in(request):
    if request.method== 'POST':
        username=request.POST['username']
        password=request.POST['password']
        
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You have successfuly logged in")
            return redirect ('home') 

    return render(request, 'auth/sign_in.html') 



def sign_out(request):
    logout(request)
    messages.success(request,"Logged out!!!")
    return redirect ('home') 




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
                first_Name = fname, 
                last_Name = lname,
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
    
    # if not request.user.is_staff:
    #     return redirect('admin-login')

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
        date = request.POST['date'] 
        time = request.POST['time'] 
        message = request.POST['message'] 
        
        doctor = Doctor.objects.filter(first_Name=doctor_name).first()
        patient = Patient.objects.filter(first_name=patient_name).first()

        try:
            Appointment.objects.create( 
                doctor = doctor,
                patient = patient, 
                date = date,
                time = time,
                message = message, 
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




# def test_request_appointment(request): 
#     error = "" 

#     doctors = Doctor.objects.all() 

#     if request.method == 'POST':
#         patient_name = request.POST['patient-name'] 
#         patient_phone = request.POST['patient-phone']
#         patient_email = request.POST['patient-email'] 
#         patient_address = request.POST['patient-address']
#         preferred_date = request.POST['preferred-date'] 
#         preferred_time = request.POST['preferred-time']
#         doctor = request.POST['doctor']  
#         appointment_message = request.POST['appointment-message'] 


#         doctor = Doctor.objects.filter(first_Name=doctor).first()

#         try:
#             Appointment.objects.create( 
#                 patient_name = patient_name,
#                 patient_phone = patient_phone,
#                 patient_email = patient_email,
#                 patient_address = patient_address,
#                 preferred_date = preferred_date,
#                 preferred_time = preferred_time,
#                 doctor_name = doctor,
#                 appointment_message = appointment_message,
#             )
#             error = "no"  

#         except:
#             error = "yes"    

        # sending email to patients
        
        # appointment = "Name: " + patient_name + "Phone Number: " + patient_phone + "Email: " + patient_email + "Address: " + patient_address + "Appointment Date: " + preferred_date + "Appointment Time: " + preferred_time + "Doctor: " + doctor_name + "Message: " + appointment_message

        # send_mail(
        #     'Appointment Request', #Subject  
        #     appointment, #Message
        #     patient_email, #From email
        #     ['kirugik79@gmail.com'], #To email
        # )
        


    #     context = {'patient_name': patient_name, 'patient_phone': patient_phone, 'patient_email': patient_email, 'patient_address': patient_address, 'preferred_date': preferred_date, 'preferred_time': preferred_time, 'doctor': doctor, 'appointment_message': appointment_message}
    #     return render(request, 'appointment/home.html', context)

    # else:
    #     context = {'doctors': doctors, 'error': error, }
    #     return render(request, 'appointment/request_appointment.html', context)
