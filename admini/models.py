from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from phone_field import PhoneField
from PIL import Image
from django_countries.fields import CountryField

# Create your models here.


class Member(models.Model):
    amci = models.CharField(max_length = 8, unique = True, default = "")
    nom = models.CharField(max_length = 50, default="")
    prenoms = models.CharField(max_length = 50, default="")
    mail = models.EmailField(max_length = 100, default="")
    date_nais = models.DateField()
    tel = PhoneNumberField(blank=True)
    annee_bourse = models.IntegerField(default = 2020)
    instagram = models.CharField(max_length = 250, default = "", blank = True)
    facebook = models.CharField(max_length = 250, default = "", blank = True)
    twitter = models.CharField(max_length = 250, default = "", blank = True)

    def __str__(self):
        return "%s" %(self.nom)



class Reunion(models.Model):
    nom = models.CharField(max_length = 60)
    pdf = models.FileField(upload_to = 'pdf')
    
    def __str__(self):
        return "%s" %(self.nom)



class Treasury(models.Model):
    nom = models.CharField(max_length = 60)
    prix = models.DecimalField(9999, max_digits = 6, decimal_places = 2)
    date = models.DateField()
    def __str__(self):
        return "%s" %(self.nom)


class BoardMembers(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    status_choices = (
        ('Super Admin', 'Super Admin'),
        ('Treasurer', 'Treasurer'),
        ('Secretary', 'Secretary'),
    )
    statut = models.CharField(max_length = 15, choices = status_choices, default = "Super Admin")
    nom = models.CharField(max_length = 50, default="")
    prenoms = models.CharField(max_length = 50, default="")
    mail = models.EmailField(max_length = 100, default="")
    date_nais = models.DateField()
    tel = PhoneNumberField(blank=True)
    def __str__(self):
        return "%s %s" %(self.nom, self.prenoms)
