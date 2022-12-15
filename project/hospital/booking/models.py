from django.db import models

# Create your models here.
class Booking(models.Model):
    pat_name=models.CharField(max_length=225, null=True)
    dot_name=models.CharField(max_length=225,null=True)
    dept_name=models.CharField(max_length=225,null=True)
    ph_no=models.CharField(max_length=10)
    symptmas=models.CharField(max_length=350)
    date = models.DateField()


    def __str__(self):
        return self.pat_name

department=[('Cardiologist','Cardiologist'),
('Dermatologists','Dermatologists'),
('Emergency Medicine Specialists','Emergency Medicine Specialists'),
('Allergists/Immunologists','Allergists/Immunologists'),
('Anesthesiologists','Anesthesiologists'),
('Colon and Rectal Surgeons','Colon and Rectal Surgeons')
]

class Department(models.Model):
    dep_name=models.CharField(max_length=220,choices=department)
    dep_desc=models.TextField()

    def __str__(self):
        return self.dep_name




class Doctors(models.Model):
    doc_name = models.CharField(max_length=225)
    doc_spec = models.CharField(max_length=225)
    doc_image = models.ImageField(upload_to='doctors')



    def __str__(self):
        return self.doc_name