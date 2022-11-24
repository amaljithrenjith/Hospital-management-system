from django.shortcuts import render,redirect
from .models import Booking,Doctors,Department


# Create your views here.

def index(request):
    return render(request,'booking/index.html')

def theme(request):
    return render(request,'booking/theme.html')

def doctors(request):
    dict_docs={
        'doctors':Doctors.objects.all()
    }
    return render(request,'booking/doctors.html',dict_docs)


def appointment(request):

    if request.method =='POST':

          name_p = request.POST.get('patientname')
          name_d  = request.POST.get('doctname')
          dept_name = request.POST.get('departname')
          ph_no = request.POST.get('phoneno')
          sytm = request.POST.get('symptoms')
          date = request.POST.get('bday')
          booking = Booking(pat_name=name_p,dot_name=name_d,dept_name=dept_name,ph_no=ph_no,symptmas=sytm,date=date)
          booking.save()

    return render(request,'booking/appointment.html')

def service(request):

    dict_dept={
        'department':Department.objects.all()

    }
    return render(request,'booking/service.html',dict_dept)


def about(request):
    return render(request,'booking/about.html')