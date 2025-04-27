from django import forms
from .models import *


class Create_doctor(forms.ModelForm):

    # name = forms.CharField(required = False,
    #                         widget = forms.TextInput(attrs= { 
    #             'class' : 'form-control',
    #             "placeholder" : "input doctor name" } )   )
    
    # email = forms.EmailField(required = False,
    #                         widget = forms.EmailInput(attrs= { 
    #             'class' : 'form-control',
    #             "placeholder" : "input email" } )   )
    
    # phone = forms.IntegerField(
    #     required=False,
    #     widget=forms.NumberInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': 'input phone number'
    #     })
    # )

    class Meta():
        model = Doctors
        fields = ["name", "email", "phone", "image"]
        widgets = {
            "name": forms.TextInput( attrs = { 
                'class' : 'form-control',
                "placeholder" : "input doctor name" }),

            "email": forms.EmailInput(attrs= { 
                "class" : "form-control",
                "placeholder" : "input email" }),

            "phone": forms.NumberInput(attrs= { 
                "class" : "form-control",
                "placeholder" : "input number" }),

            "image": forms.ClearableFileInput(attrs={
                "class": "form-control" })

        }
