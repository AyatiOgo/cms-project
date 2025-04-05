from django.shortcuts import render
from .models import Doctors, Patients
from .forms import Create_doctor
# from .filters import Doctor_filter

# Create your views here.

def home_view(request):
    total_docs = Doctors.objects.count()
    total_patients = Patients.objects.count()

    context = {
        "total_docs" : total_docs,
        "total_patients" : total_patients
    }

    return render(request, "home.html", context)


def doctors_view(request):
    doctors = Doctors.objects.all()
    # filters = Doctor_filter()
    context = {"doctors": doctors }

    return render(request, "doctor-list.html", context)

def patients_view(request):
    patients = Patients.objects.all()

    context = {"patients": patients }

    return render(request, "patient_list.html", context)


def doctor_create(request):
    form = Create_doctor(request.POST, request.FILES) 
    if form.is_valid():
        form.save()
    return render(request, "create_doctor.html", {"form": form})