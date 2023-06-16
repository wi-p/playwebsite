from django.db import models
from django.utils.text import slugify

# Create your models here.

class GameCompany(models.Model):
    name = models.CharField(max_length = 50)
    date_foundation = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.name


class TypeGameStation(models.Model):
    name = models.CharField(max_length = 50)
    date_foundation = models.DateField()
    description = models.TextField()
    game_company = models.ForeignKey(GameCompany, on_delete = models.CASCADE)

    def __str__(self):
        return self.name
                    
        
class VideoGame(models.Model):
    name = models.CharField(max_length = 50)
    date_foundation = models.DateField()
    description = models.TextField()
    game_station = models.ManyToManyField(TypeGameStation, through = 'GameStationHasGame')
    game_company = models.ForeignKey(GameCompany, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.name


class GameStationHasGame(models.Model):
    video_game = models.ForeignKey(VideoGame, on_delete = models.CASCADE)
    game_company = models.ForeignKey(TypeGameStation, on_delete = models.CASCADE)


class GameNews(models.Model):
    title = models.CharField(max_length = 100)
    date = models.DateField()
    content = models.TextField()
    game = models.ForeignKey(VideoGame, on_delete = models.CASCADE)
    photo = models.FileField(upload_to = "images/uploaded/")
    url = models.SlugField(null = True, blank = True)

    def __str__(self):
        return self.title
        
    def save(self, *args, **kwargs):  # new
        if not self.url:
            self.url = slugify(self.title)
        
        return super().save(*args, **kwargs)


class GameReview(models.Model):
    title = models.CharField(max_length = 100)
    data = models.DateField()
    review = models.TextField()
    game = models.ForeignKey(VideoGame, on_delete = models.CASCADE)

    def __str__(self):
        return self.title