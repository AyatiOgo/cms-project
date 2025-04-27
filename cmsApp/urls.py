from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view  ,name="home"),
    path('form_doctor/', doctor_create  ,name="create_doctor"),
    path('doctors/', doctors_view  ,name="doctors_view"),
    path('patients/', patients_view  ,name="patients_view"),
]