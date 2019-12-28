from django.shortcuts import render
from gameplay.models import Game

# Create your views here.
def home(request):
    list_games=list(Game.objects.filter(first_player=request.user, status='F'))+list(Game.objects.filter(second_player=request.user, status='S'))
    return render(request,'player/home.html',{'games':list_games})
