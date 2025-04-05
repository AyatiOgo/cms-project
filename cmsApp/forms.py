from django import forms
from .models import *


class Create_doctor(forms.ModelForm):

    class Meta():
        model = Doctors
        fields = ["name", "email", "phone", "image"]
