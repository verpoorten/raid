from django import forms
from django.forms import ModelForm
from main.models import Inscription

class InscriptionForm(ModelForm):

    class Meta:
        model = Inscription
        fields=['nom_equipe','nom_participant_1','nom_participant_2','categorie','responsable_email','responsable_telephone','challenge_raid_trophy',
        'taille_t_shirt_1','taille_t_shirt_2','reglement_ok']
