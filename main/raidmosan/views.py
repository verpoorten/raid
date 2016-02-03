from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, "home.html")

def reglement(request):
    return render(request, 'reglement.html')

def inscription(request):
    return render(request, 'inscription.html')

def inscription_add(request):
    inscription = Inscription()

    inscription.nom_equipe = request.POST['nom_equipe']
    inscription.nom_participant_1 = request.POST['nom_participant_1']
    inscription.nom_participant_2 = request.POST['nom_participant_2']
    inscription.categorie = request.POST['categorie']
    inscription.responsable_email = request.POST['responsable_email']
    inscription.responsable_telephone = request.POST['responsable_telephone']
    inscription.challenge_raid_trophy = request.POST['challenge_raid_trophy']
    inscription.taille_t_shirt = request.POST['taille_t_shirt']
    inscription.reglement_ok = request.POST['reglement_ok']


    inscription.save()

    return render(request, 'inscription_list.html',{'inscriptions':Inscription.objects.all()})
    
def inscriptions(request):
    return render(request, 'inscription_list.html',{'inscriptions':Inscription.objects.all()})
