from django.db import models
from django.utils import timezone
import datetime

class Inscription(models.Model):
    TAILLE = (
        ('S','Small'),
        ('M','Medium'),
        ('L','Large'),
        ('XL','Extra large'),
    )
    CATEGORIE = (
        ('DAMES','Dames'),
        ('HOMMES','Hommes'),
        ('MIXTE','Mixte')
    )
    nom_equipe            = models.CharField(max_length = 100, blank = False, null = False, unique=True,  error_messages={'unique':"Ce nom d'équipe existe déjà."})
    nom_participant_1     = models.CharField(max_length = 50, blank = False, null = False, error_messages={'required':"Nom du participant 1 obligatoire"})
    nom_participant_2     = models.CharField(max_length = 50, blank = False, null = False, error_messages={'required':"Nom du participant 2 obligatoire"})
    categorie             = models.CharField(max_length = 6, choices = CATEGORIE, blank = False, null = False, error_messages={'required':"Catégorie obligatoire"})
    responsable_email     = models.EmailField( blank = False, null = False)
    responsable_telephone = models.CharField(max_length = 30, blank = False, null = False)
    challenge_raid_trophy = models.BooleanField(default = False)
    taille_t_shirt_1      = models.CharField(max_length = 6, choices = TAILLE, blank = False, null = False, error_messages={'required':"Catégorie obligatoire"})
    taille_t_shirt_2      = models.CharField(max_length = 6, choices = TAILLE,blank = False, null = False, error_messages={'required':"Catégorie obligatoire"})
    reglement_ok          = models.BooleanField(default = False)
    inscription_validee   = models.BooleanField(default = False)

    def __str__(self):
        return self.nom_equipe
    class Meta:
        ordering = ['nom_equipe']
