from django.shortcuts import render, redirect
from .forms import PayForm
from django.contrib import messages

from main.models import Game
def add_money(request):
    form = PayForm()
    
    
    if request.method == "POST":
        form=PayForm(request.POST)
        
        if form.is_valid():
            user = request.user
            

            if user.balls != None:
                user.balls += 0.1 * int(form.cleaned_data["money"])
            else:
                user.balls = 0.1 * int(form.cleaned_data["money"])
            if user.money != None:
                user.money += int(form.cleaned_data["money"])
            else:
                user.money = int(form.cleaned_data["money"])

            user.save()

            return redirect("main")
        else:
            error=form.errors
    context = {
        "form" : form

    }
    return render(request, "payment/add_money.html", context=context)

def payment(request, game_id):
    
    game=Game.objects.get(id=game_id)
    error=""
    
    if game.price > request.user.balls:
        price = game.price - request.user.balls
        if request.user.money >= price:
            request.user.money -= price
            request.user.balls = 0
            request.user.buyed_games.add(game)
            request.user.save()
            messages.success(request, "Вы успешно купили игру")
            return redirect("main")
        else:
            messages.error(request, "На балансе недостаточно средств")
    else:
        request.user.balls -= game.price
        request.user.buyed_games.add(game)
        request.user.save()
        messages.success(request, "Вы купили игру за баллы")
    return redirect("main")
    
# Create your views here.
