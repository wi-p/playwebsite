from django.shortcuts import render
from .models import GameNews, VideoGame
# Create your views here.

def index(request):
    return render(request, 'website/index.html',
                  {'gamenews' : GameNews.objects.all(),
                   'videogames' : VideoGame.objects.all()}
    )
                  
def post(request, post):
    return render(request,
                  'website/post.html',
                  {'new' : GameNews.objects.get(url = post)}
    )


