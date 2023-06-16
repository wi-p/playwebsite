from django.contrib import admin
from .models import GameCompany, TypeGameStation, VideoGame, GameNews, GameReview

# Register your models here.

admin.site.register(GameCompany)
admin.site.register(TypeGameStation)
admin.site.register(VideoGame)
admin.site.register(GameNews)
admin.site.register(GameReview)