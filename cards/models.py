from django.db import models
from django.conf import settings


class TagManager(models.Manager):
    def get_by_natural_key(self, Name):
        return self.get(Name=Name)

class CardManager(models.Manager):
    def get_by_natural_key(self, Name):
        return self.get(Name=Name)

class DeckManager(models.Manager):
    def get_by_natural_key(self, Name,*args):
        return self.get(Name=Name)
    
class SpotManager(models.Manager):
    def get_by_natural_key(self, Name, *args):
        return self.get(Name=Name)

class VisibilityManager(models.Manager):
    def get_by_natural_key(self, Name):
        return self.get(Name=Name)

class RowManager(models.Manager):
    def get_by_natural_key(self, Name):
        return self.get(Name=Name)

class GameManager(models.Manager):
    def get_by_natural_key(self, Name):
        return self.get(Name=Name)

class Tag(models.Model):
    objects = TagManager()
    
    Name = models.CharField(max_length=80)
    def __unicode__(self):
        return self.Name
    def natural_key(self):
        return (self.Name,)

class Card(models.Model):
    objects = CardManager()
    
    Name = models.CharField(max_length=80)
    Tags = models.ManyToManyField(Tag)
    def __unicode__(self):
        return self.Name
    def natural_key(self):
        return (self.Name,)
    
class Deck(models.Model):
    objects = DeckManager()
    
    Name = models.CharField(max_length=80)
    Cards = models.ManyToManyField(Card)
    def __unicode__(self):
        return self.Name
    def natural_key(self):
        return (self.Name,)
    
class Spot(models.Model):
    objects = SpotManager()
    
    Name = models.CharField(max_length=80,blank=True,null=True)
    Drop =  models.BooleanField(default=False)
    Deck = models.ForeignKey(Deck,null=True)
    def __unicode__(self):
        return self.Name
    def natural_key(self):
        return (self.Name,)
    
class Visibility(models.Model):
    objects = VisibilityManager()
    
    Name = models.CharField(max_length=80,blank=True,null=True)
    Description = models.CharField(max_length=255,blank=True,null=True)
    def __unicode__(self):
        return self.Name
    def natural_key(self):
        return (self.Name,)
    
class Row(models.Model):
    objects = RowManager()
    
    Name = models.CharField(max_length=80,blank=True,null=True)
    Spots = models.ManyToManyField(Spot)
    NewRow =  models.BooleanField(default=False)
    Width = models.IntegerField(default=-1)
    Visibility = models.ForeignKey(Visibility,null=True)
    def __unicode__(self):
        return self.Name
    def natural_key(self):
        return (self.Name,)
    
class Game(models.Model):
    objects = GameManager()
    
    Name = models.CharField(max_length=80)
    Rows = models.ManyToManyField(Row)
    def __unicode__(self):
        return self.Name
    def natural_key(self):
        return (self.Name,)
    
class GameInstance(models.Model):
    Game = models.ForeignKey(Game)
    Players = models.ManyToManyField(settings.AUTH_USER_MODEL)
    State = models.TextField(blank=True)
    def __unicode__(self):
        return "Instance {} of {}".format(self.id,self.Game.Name)

class Invitation(models.Model):
    GameInstance = models.ForeignKey(GameInstance)
    Target = models.ForeignKey(settings.AUTH_USER_MODEL)
    def __unicode__(self):
        return "Invitation to {}".format(str(self.GameInstance))


