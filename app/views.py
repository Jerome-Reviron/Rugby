from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from app.models import Club
from app.models import Player

def index(request):
    # Récupérer tous les clubs
    all_clubs = Club.objects.all()

    # Nombre de clubs par page
    clubs_per_page = 7

    # Utiliser la pagination
    paginator = Paginator(all_clubs, clubs_per_page)
    page = request.GET.get('page')

    try:
        clubs = paginator.page(page)
    except PageNotAnInteger:
        # Si la page n'est pas un entier, afficher la première page
        clubs = paginator.page(1)
    except EmptyPage:
        # Si la page est hors de portée (par exemple, 9999), afficher la dernière page
        clubs = paginator.page(paginator.num_pages)

    context = {'clubs': clubs}
    return render(request, 'index.html', context)

def licences(request):
    # Récupérer tous les players
    all_players = Player.objects.all()

    # Nombre de players par page
    players_per_page = 3

    # Utiliser la pagination
    paginator = Paginator(all_players, players_per_page)
    page = request.GET.get('page')

    try:
        players = paginator.page(page)
    except PageNotAnInteger:
        # Si la page n'est pas un entier, afficher la première page
        players = paginator.page(1)
    except EmptyPage:
        # Si la page est hors de portée (par exemple, 9999), afficher la dernière page
        players = paginator.page(paginator.num_pages)

    context = {'players': players}
    return render(request, 'licences.html', context)