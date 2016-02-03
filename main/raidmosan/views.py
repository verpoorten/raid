from django.shortcuts import render
from django.http import HttpResponse
from raidmosan.models import Inscription

def home(request):
    return render(request, "home.html")

def reglement(request):
    return render(request, 'reglement.html')

def contact(request):
    return render(request, 'contact.html')

def inscription(request):
    print('inscription')
    return render(request, 'inscription.html')

def photos(request):
    print('photos')
    return render(request, 'photos.html')

def inscriptions(request):
    print('inscriptions')
    return render(request, 'inscription_list.html')

def inscriptions2(request):
    print('inscriptions2')
    return render(request, 'inscription_list.html')

def inscription_add(request):
    print('inscription_add')
    inscription = Inscription()
    print('1')
    inscription.nom_equipe = request.POST['nom_equipe']
    print('12')
    inscription.nom_participant_1 = request.POST['nom_participant_1']
    print('13')
    inscription.nom_participant_2 = request.POST['nom_participant_2']
    print('14')
    inscription.categorie = request.POST['categorie']
    print('15')
    inscription.responsable_email = request.POST['responsable_email']
    print('1')
    inscription.responsable_telephone = request.POST['responsable_telephone']
    print('1')
    if request.POST['reglement_ok']:
        print('if')
        inscription.reglement_ok = request.POST['reglement_ok']
    else:
        print ('else1')

    if request.POST['challenge_raid_trophy']:
        print('if2')
        inscription.challenge_raid_trophy = request.POST['challenge_raid_trophy']
    else:
        print ('else2')
    print('1')
    inscription.taille_t_shirt_1 = request.POST['taille_t_shirt_1']
    print('1')
    inscription.taille_t_shirt_2 = request.POST['taille_t_shirt_2']

    inscription.save()

    return render(request, 'test.html',{'inscriptions':Inscription.objects.all()})

def classement(request):
    print('classement')
    return render(request, 'classement.html')

def test(request):
    return render(request, 'test.html',{'inscriptions':Inscription.objects.all()})
