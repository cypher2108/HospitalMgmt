from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from hospital.models import *


def about(request):
    return render(request, 'about.html')


def home(request):
    return render(request, 'home.html')


def Index(request):
    if not request.user.is_authenticated:
        return redirect('index')
    return render(request, 'index.html')


def Login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)

        if user:
            login(request, user)
            error = "no"
            return render(request, 'home.html')
        else:
            error = "yes"

    d = {'error': error}
    return render(request, 'login.html', d)


def Logout_admin(request):
    if not request.user.is_authenticated:
        return redirect('login')
    logout(request)
    return redirect('home')


def Contact(request):
    return render(request, 'contact.html')


def view_doctor(request):
    if not request.user.is_authenticated:
        return redirect('login')
    doc = Doctor.objects.all()
    d = {'doc': doc}
    return render(request, 'view_doctor.html', d)


def add_doctor(request):
    error = ""
    if not request.user.is_authenticated:
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
    if not request.user.is_authenticated:
        return redirect('login')
    doctor = Doctor.objects.get(id=pid)
    doctor.delete()
    return redirect('view_doctor')


def view_patient(request):
    if not request.user.is_authenticated:
        return redirect('login')
    patient = Patient.objects.all()
    p = {'patient': patient}
    return render(request, 'view_patient.html', p)


def add_patient(request):
    error = ""
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        name = request.POST['name']
        gender = request.POST['gender']
        mobile = request.POST['mobile']
        age = request.POST['age']
        email = request.POST['email']
        address = request.POST['address']

        try:
            Patient.objects.create(name=name, gender=gender, mobile=mobile, age=age, email=email, address=address)
            error = "no"

        except:
            error = "yes"
    p = {'error': error}
    return render(request, 'add_patient.html', p)


def delete_patient(request, patientid):
    if not request.user.is_authenticated:
        return redirect('login')
    patient = Patient.objects.get(id=patientid)
    patient.delete()
    return redirect('view_patient')


def view_appointment(request):
    if not request.user.is_authenticated:
        return redirect('login')
    appointment = Appointment.objects.all()
    a = {'appointment': appointment}
    return render(request, 'view_appointment.html', a)


def add_appointment(request):
    error = ""
    if not request.user.is_authenticated:
        return redirect('login')

    doctor1 = Doctor.objects.all()
    patient1 = Patient.objects.all()

    if request.method == 'POST':
        d = request.POST['doc']
        p = request.POST['pat']
        status = request.POST['status']
        date = request.POST['date']
        time = request.POST['time']
        doctor = Doctor.objects.filter(name=d).first()
        patient = Patient.objects.filter(name=p).first()
        try:
            Appointment.objects.create(doctor=doctor, patient=patient, status=status, date=date, time=time)
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


def register(request):
    error = ""
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['user_name']
        email_address = request.POST['email_address']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        register_as = request.POST['register_as']
        try:
            user = User.objects.create_user(username=username, email=email_address, password=password,
                                            first_name=first_name, last_name=last_name)
            if register_as == 'Doctor':
                user.is_staff = True
            user.save()
            error = "no"
        except:
            error = "yes"
    p = {'error': error}
    return render(request, 'register.html', p)


def dashboard(request):
    appointment = Appointment.objects.all()
    patient = Patient.objects.all()
    pending = 0
    completed = 0
    total = 0
    for i in appointment:
        total += 1

        if i.status == 'Completed':
            completed += 1
        if i.status == 'Pending':
            pending += 1

    x = {'appointment': appointment, 'patient': patient, 'completed': completed, 'pending': pending, 'total': total}
    return render(request, 'dashboard.html', x)


def doc_appointment(request):
    if not request.user.is_authenticated:
        return redirect('login')
    doc = request.user.first_name
    appointment = Appointment.objects.all()
    a = {'appointment': appointment, 'doc': doc}
    return render(request, 'view_appointment.html', a)


