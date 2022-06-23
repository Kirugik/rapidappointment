from django.db import models


GENDER = [
    ('', ('Choose')), 
    ('Male', ('Male')),
    ('Female', ('Female')),] 

# Create your models here.
class Doctor(models.Model):
    first_Name = models.CharField(max_length=100)
    last_Name = models.CharField(max_length=100) 
    gender = models.CharField(choices=GENDER, max_length=50) 
    department = models.CharField(max_length=50)
    specialty = models.CharField(max_length=50)
    phone = models.IntegerField() 
    address = models.CharField(max_length=100)
    
    def __str__(self):
        return self.first_Name  
    


class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(choices=GENDER, max_length=50)
    phone = models.IntegerField()
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=100)  

    def __str__(self):
        return self.first_name  



class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField(null=True) 
    time = models.TimeField() 
    message = models.TextField(max_length=300, null=True)   
    # approved = models.BooleanField('Approved', default=False)   
    date_sent = models.DateField(auto_now_add=True, null=True)
    date_approved = models.DateField(auto_now_add=False, null=True, blank=True) 


    def __str__(self):
        return self.patient.first_name 
    
    class Meta:
        ordering = ["-date_sent"]
