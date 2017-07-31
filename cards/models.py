from django.db import models


class Spot(models.Model):
    Name = models.CharField(max_length=80,blank=True,null=True)
    Drop =  models.BooleanField(default=False)

class Visibility(models.Model):
    Name = models.CharField(max_length=80,blank=True,null=True)
    Description = models.CharField(max_length=255,blank=True,null=True)

class Row(models.Model):
    Name = models.CharField(max_length=80,blank=True,null=True)
    Spots = models.ManyToManyField(Spot)
    NewRow =  models.BooleanField(default=False)
    Width = models.IntegerField(default=-1)
    Visibility = models.ForeignKey(Visibility,null=True)
    
class Game(models.Model):
    Name = models.CharField(max_length=80)
    Rows = models.ManyToManyField(Row)
    
class GameInstance(models.Model):
    pass

class Card(models.Model):
    Name = models.CharField(max_length=80)
    
class Deck(models.Model):
    Name = models.CharField(max_length=80)
    Cards = models.ManyToManyField(Card)
    
