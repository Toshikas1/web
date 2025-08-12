from django.db import models
from django.contrib.auth.models import AbstractUser


class Game(models.Model):
    name=models.CharField(max_length=35)
    price=models.FloatField()
    description = models.TextField()
    release_date = models.DateField( auto_now=False, auto_now_add=False)
    img1 = models.ImageField( upload_to="games/images", blank=True, null=True)
    img2 = models.ImageField( upload_to="games/images", blank=True, null=True)
    img3 = models.ImageField(upload_to="games/images", blank=True, null=True)
    logo=models.ImageField( upload_to="games/logos", blank=True, null=True)
    trailer = models.FileField( upload_to="games/trailers", blank=True, null=True)
    genre = models.CharField( max_length=50)
    creator=models.CharField( max_length=50)
    rating=models.DecimalField( max_digits=3, decimal_places=1)
    def __str__(self):
        return self.name
class CustomUser(AbstractUser):
    balls = models.IntegerField(blank = True, null=True)
    money = models.IntegerField(blank = True, null=True)
    buyed_games = models.ManyToManyField(Game, blank = True, null = True, related_name="buyed_by")
