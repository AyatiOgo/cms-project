from django.db import models

# Create your models here.
class Doctors(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    phone = models.CharField(max_length=25)
    image = models.ImageField(max_length=250, null=True, blank= True)
    class Meta:
        db_table = "Doctors"
    
    def __str__(self):
        return self.name

    


class Patients(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    phone = models.CharField(max_length=25)
    image = models.ImageField(max_length=250, null=True, blank=True)
    doctor = models.ForeignKey(Doctors, on_delete= models.CASCADE)
    class Meta:
        db_table = "Patients"

    def __str__(self):
        return self.name




