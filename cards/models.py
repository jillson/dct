from django.db import models
from django.conf import settings

class Tag(models.Model):
    Name = models.CharField(max_length=80)

class Card(models.Model):
    Name = models.CharField(max_length=80)
    Tags = models.ManyToManyField(Tag)
    
class Deck(models.Model):
    Name = models.CharField(max_length=80)
    Cards = models.ManyToManyField(Card)

class Spot(models.Model):
    Name = models.CharField(max_length=80,blank=True,null=True)
    Drop =  models.BooleanField(default=False)
    Deck = models.ForeignKey(Deck,null=True)


class Visibility(models.Model):
    Name = models.CharField(max_length=80,blank=True,null=True)
    Description = models.CharField(max_length=255,blank=True,null=True)

class Row(models.Model):
    Name = models.CharField(max_length=80,blank=True,null=True)
    Spots = models.ManyToManyField(Spot)
    NewRow =  models.BooleanField(default=False)
    Width = models.IntegerField(default=-1)
    Visibility = models.ForeignKey(Visibility,null=True)

    def serialize(self):
        data = {
            'name': self.Name,
            'spots': [x.serialize() for x in self.Spots.all()],
            'newRow': self.NewRow
        }
        if self.Visibility:
            data["visibility"] = self.Visibility.Name
        if self.Width >= 0:
            data["width"] = self.Width
        return data
    
class Game(models.Model):
    Name = models.CharField(max_length=80)
    Rows = models.ManyToManyField(Row)
    
class GameInstance(models.Model):
    Game = models.ForeignKey(Game)
    Players = models.ManyToManyField(settings.AUTH_USER_MODEL)
    State = models.TextField(blank=True)

class Invitation(models.Model):
    GameInstance = models.ForeignKey(GameInstance)
    Target = models.ForeignKey(settings.AUTH_USER_MODEL)


