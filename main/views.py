from django.shortcuts import render, redirect
from django.http import HttpResponse
from.models import Game
from.forms import GameForm
from django.contrib.auth.decorators import login_required
def about(request):
    return render(request, "main/about.html")
# Create your views here.
def main(request):
    user= request.user
    games = Game.objects.all()
    
    context = {
        "authors" : ["Anton", "Sergei"],
        "games" : games
    }


    return render(request, template_name="main/home.html", context=context)
def game_details(request, game_id):
    game=Game.objects.get(id=game_id)
    if game.buyed_by.filter(id=request.user.id).exists():
        is_buyed = True
    else:
        is_buyed = False
    context={
        "game" : game,
        "is_buyed" : is_buyed
    }
    return render(request, "main/game_details.html", context=context)
@login_required (login_url='/account/login/')
def add_game(request):
    form = GameForm()
    error=""
    
    
    if request.method == "POST":
        form=GameForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect("main")
        else:
            error=form.errors
    context={
        "form" : form,
        "error" : error
    }


    return render(request, "main/add_game.html", context=context)

