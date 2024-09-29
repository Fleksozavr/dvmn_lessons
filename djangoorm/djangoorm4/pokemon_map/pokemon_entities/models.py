from django.db import models  # noqa F401
from django.utils import timezone


class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.title
    

class PokemonEntity(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()

    appeared_at = models.DateTimeField(default=timezone.now)
    disappeared_at = models.DateTimeField(null=True)

    level = models.IntegerField(default=1)
    health = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    stamina = models.IntegerField()

    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)