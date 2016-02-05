from django.shortcuts import render
from django.http import HttpResponse
from raidmosan.models import Inscription
from django.core.exceptions import ValidationError

def home(request):
    return render(request, "home.html")

def reglement(request):
    return render(request, 'reglement.html')

def contact(request):
    return render(request, 'contact.html')

def inscription(request):
    return render(request, 'inscription.html'
                         ,{'inscription': Inscription(),
                            'messages'  : dict()})

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

    nouvelle_inscription = Inscription()
    nouvelle_inscription.nom_equipe = request.POST['nom_equipe']
    nouvelle_inscription.nom_participant_1 = request.POST['nom_participant_1']
    nouvelle_inscription.nom_participant_2 = request.POST['nom_participant_2']
    nouvelle_inscription.categorie = request.POST['categorie']
    nouvelle_inscription.responsable_email = request.POST['responsable_email']
    nouvelle_inscription.responsable_telephone = request.POST['responsable_telephone']

    if request.POST.get('reglement_ok', False): # will be True if checked
        nouvelle_inscription.reglement_ok = True
    else:
        nouvelle_inscription.reglement_ok = False

    if request.POST.get('challenge_raid_trophy', False):
        nouvelle_inscription.challenge_raid_trophy = True
    else:
        nouvelle_inscription.challenge_raid_trophy = False

    nouvelle_inscription.taille_t_shirt_1 = request.POST['taille_t_shirt_1']

    nouvelle_inscription.taille_t_shirt_2 = request.POST['taille_t_shirt_2']
    dict_msg_error = dict()
    if  not nouvelle_inscription.reglement_ok:
        dict_msg_error["reglement_ok"] = "Il faut accepter le réglement"
    try:
        nouvelle_inscription.full_clean()
        if len(dict_msg_error.keys()) >0:
            return render(request, 'inscription.html',{
                        'inscription': nouvelle_inscription,
                        'messages' : dict_msg_error})
    except ValidationError as e:
        # Do something based on the errors contained in e.message_dict.
        # Display them to a user, or handle them programmatically.
        print(e)
        dict_errors = dict(e)
        if dict_errors.get('nom_equipe'):
            dict_msg_error["nom_equipe"] = "Le nom d'équipe existe déjà"
        if dict_errors.get('categorie'):
            dict_msg_error["categorie"] = "Il faut sélectionner une catégorie"
        if dict_errors.get('taille_t_shirt_1'):
            dict_msg_error["taille_t_shirt_1"] = "Il faut sélectionner une taille de t-shirt 1"
        if dict_errors.get('taille_t_shirt_2'):
            dict_msg_error["taille_t_shirt_2"] = "Il faut sélectionner une taille de t-shirt 2"
        if dict_errors.get('responsable_email'):
            dict_msg_error["responsable_email"] = "L'adresse email encodée semble incorrect"


        nom_equipe_error_message='error'
        return render(request, 'inscription.html',{
                    'inscription': nouvelle_inscription,
                    'messages' : dict_msg_error})
        pass
    nouvelle_inscription.save()

    return render(request, 'test.html',{'inscriptions':Inscription.objects.all()})

def classement(request):
    return render(request, 'classement.html')

def test(request):
    return render(request, 'test.html',{'inscriptions':Inscription.objects.all()})

def xls_inscriptions(request):
    short_description = "Export excel"
