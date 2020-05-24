from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render, redirect

# Create your views here.
from hospital.models import *


def about(request):
    return render(request, 'about.html')


def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    return render(request, 'index.html')


def Login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)

        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'login.html', d)


def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')


def Contact(request):
    return render(request, 'contact.html')


def view_doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Doctor.objects.all()
    d = {'doc': doc}
    return render(request, 'view_doctor.html', d)


def add_doctor(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')

    if request.method == 'POST':
        name = request.POST['name']
        contact = request.POST['contact']
        specialization = request.POST['special']

        try:
            Doctor.objects.create(name=name, mobile=contact, specialization=specialization)
            error = "no"

        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'add_doctor.html', d)


def delete_doctor(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    doctor = Doctor.objects.get(id=pid)
    doctor.delete()
    return redirect('view_doctor')


def view_patient(request):
    if not request.user.is_staff:
        return redirect('login')
    patient = Patient.objects.all()
    p = {'patient': patient}
    return render(request, 'view_patient.html', p)


def add_patient(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')

    if request.method == 'POST':
        name = request.POST['name']
        gender = request.POST['gender']
        mobile = request.POST['mobile']
        address = request.POST['address']

        try:
            Patient.objects.create(name=name, gender=gender, mobile=mobile, address=address)
            error = "no"

        except:
            error = "yes"
    p = {'error': error}
    return render(request, 'add_patient.html', p)


def delete_patient(request, patientid):
    if not request.user.is_staff:
        return redirect('login')
    patient = Patient.objects.get(id=patientid)
    patient.delete()
    return redirect('view_patient')


def view_appointment(request):
    if not request.user.is_staff:
        return redirect('login')
    appointment = Appointment.objects.all()
    a = {'appointment': appointment}
    return render(request, 'view_appointment.html', a)


def add_appointment(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')

    doctor1 = Doctor.objects.all()
    patient1 = Patient.objects.all()

    if request.method == 'POST':
        d = request.POST['doc']
        p = request.POST['pat']
        date = request.POST['date']
        time = request.POST['time']
        doctor = Doctor.objects.filter(name=d).first()
        patient = Patient.objects.filter(name=p).first()
        try:
            Appointment.objects.create(doctor=doctor, patient=patient, date=date, time=time)
            error = "no"

        except:
            error = "yes"
    x = {'doctor': doctor1, 'patient': patient1, 'error': error}
    return render(request, 'add_appointment.html', x)


def delete_appointment(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    appointment = Appointment.objects.get(id=pid)
    appointment.delete()
    return redirect('view_appointment')
