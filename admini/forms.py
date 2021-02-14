from django import forms
from admini.models import Member
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField
from django_countries.fields import CountryField


### Class django pour afficher le calendrier au niveau du formulaire
class dateInput(forms.DateInput):
####Le formulaire pour l'inscription du candidat####
    input_type = 'date'
class memberForm(forms.Form):
    amci = forms.CharField(max_length = 8, label = "AMCI")
    fname = forms.CharField(max_length = 50, label = "Nom")
    lname = forms.CharField(max_length = 50, label = "Prénom")
    mail = forms.EmailField(max_length = 60, label = "Adresse mail")
    date_nais = forms.DateField(label = "Date de naissance", widget = dateInput)
    tel = PhoneNumberField(max_length = 15, label = "Téléphone")
    annee_bourse = forms.IntegerField(label = "Année d'attribution de la bourse")
    instagram = forms.CharField(max_length = 60, label = "Instagram", required = False)
    facebook = forms.CharField(max_length = 60, label = "Facebook", required = False)
    twitter = forms.CharField(max_length = 60, label = "Twitter", required = False)


class treasuryForm(forms.Form):
    nom = forms.CharField(max_length = 60, label = "Nom du produit")
    prix = forms.DecimalField(label = "Prix")
    date = forms.DateField(widget = dateInput, label = "Date d'achat")


class meetingForm(forms.Form):
    nom = forms.CharField(max_length = 60, label = "Objet de la reunion")
    pdf = forms.FileField(label = "Compte rendu de la reunion")
