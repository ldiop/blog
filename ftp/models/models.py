
from django.db import models
from phone_field import PhoneField
from datetime import datetime

# Create your models here.

class T_user(models.Model):
    idUser = models.AutoField(primary_key=True )
    ftpUsername = models.CharField(max_length=100, unique=True)
    ftpPassword = models.CharField(max_length=50)
    ftpHomeDir  = models.CharField(max_length=100)

    FTPSTATUS = (
        (1, 'Actif'),
        (0, 'Inactif'),
    )

    actif = models.PositiveSmallIntegerField(choices=FTPSTATUS, default=1)
    dateCreation = models.DateTimeField(auto_now_add=True, null=True)
    dateExpiration = models.DateTimeField(default= datetime(2025, 6, 15))

    #dateExpiration = models.DateTimeField(default=datetime.now())
    dateAcces = models.DateTimeField(auto_now=True, null=True, blank=True)
    nom =  models.CharField(max_length=20)
    societe =  models.CharField(max_length=20)
    email = models.EmailField(null=True, blank=True)
    telephone = models.CharField(max_length=20)
    permanent = models.PositiveSmallIntegerField(default=1)
    ftpGroup  = models.CharField(max_length=200, null=True, blank=True)
    idAdministrateur = models.PositiveSmallIntegerField(default=8)
    contact_interne = models.CharField(max_length=255, null=True, blank=True)
    FILESTATUS = (
        (1, 'Actif'),
        (0, 'Inactif'),
    )
    filewatch_enable = models.PositiveSmallIntegerField(choices=FILESTATUS, default=1)
    filewatch_contact = models.CharField(max_length=255)
    DELSTATUS = (
        (1, 'Actif'),
        (0, 'Inactif'),
    )
    autodel_enable = models.PositiveSmallIntegerField(choices=DELSTATUS, default=1)
    autodel_range = models.IntegerField(default=11)
    autoresetpass_enable = models.IntegerField(default=10)
    autoresetpass_period = models.IntegerField(default=10)

