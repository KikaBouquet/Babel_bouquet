from django.shortcuts import render
from django.conf import settings
import json
from catalog.models import Dewey, Publication

# Create your views here.

CONTEXT_GLOBAL = {
    "mediatheque_name": "Bibliothèque de St Pons",
    "mediatheque_adress": "Villeneuve les Avignon",
    "dev_github": "https://github.com/KikaBouquet/Babel_bouquet.git",
        "dev_name": "Kika Bouquet",
}


def index(request):
    context_local = {
        "jumbotron_title": "Bienvenue sur la page d'accueil",
        "jumbotron_p": "Vous aurez toutes les informations plus tard",
    }
    context_page = {"global": CONTEXT_GLOBAL, "local": context_local}
    return render(request, "catalog/index.html", context=context_page)


def newsroom(request):
    basedir = settings.BASE_DIR
    filename = basedir + "/scrap/checkurl.json"
    try:
        with open(filename, "r") as f:
            dict_checkurl = json.load(f)
    except Exception as e:
        dict_checkurl = {"error": str(e)}

    context_local = {
        "jumbotron_title": "Bienvenue sur la newsroom",
        "jumbotron_p": "Vous aurez toutes les informations plus tard",
    }

    context_page = {"global": CONTEXT_GLOBAL, "local": context_local, 'checkurl': dict_checkurl,}

    return render(request, "catalog/newsroom.html", context=context_page)


def about(request):
    context_local = {
        "jumbotron_title": "Bienvenue sur la page d'informations",
        "jumbotron_p": "Vous aurez toutes les informations plus tard",
    }
    context_page = {"global": CONTEXT_GLOBAL, "local": context_local}
    return render(request, "catalog/about.html", context=context_page)


def publication(request):
    try:
        record = Dewey.objects.get(number='100')
        record_list = Dewey.objects.all()
        publication_list = Publication.objects.all()
    except:
        record = record_list = publication_list = None

    context_local = {
        "jumbotron_title": "Toutes les publications",
        "jumbotron_p": "Vous aurez toutes les informations plus tard",
        "title": "Tous les ouvrages"
    }
    context_page = {
        "global": CONTEXT_GLOBAL, 
        "local": context_local, 
        'dewey_object': record, 
        'dewey_object_list': record_list, 
        'publication_object_list': publication_list,
    }
    return render(request, "catalog/publications.html", context=context_page)
