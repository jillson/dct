from rest_framework import serializers

from .models import Game, GameInstance, Row, Spot, Deck, Card, Invitation

class CardSerializer(serializers.ModelSerializer):
     class Meta:
          model = Card
          fields = '__all__'

class DeckSerializer(serializers.ModelSerializer):
     Cards = CardSerializer(many=True)
     class Meta:
          model = Deck
          fields = '__all__'
          
class SpotSerializer(serializers.HyperlinkedModelSerializer):
     Deck = DeckSerializer()
     class Meta:
          model = Spot
          fields = ('Name','Drop','Deck')


class RowSerializer(serializers.HyperlinkedModelSerializer):
     Spots = SpotSerializer(many=True)
     Visibility = serializers.ReadOnlyField(source='Visibility.Name')
     class Meta:
          model = Row
          fields = ('Name','Spots','NewRow',"Width","Visibility")


class GameSerializer(serializers.HyperlinkedModelSerializer):
     Rows = RowSerializer(many=True)
     class Meta:
         model = Game
         fields = ('Name','Rows','url')


class GameInstanceSerializer(serializers.ModelSerializer):
     class Meta:
         model = GameInstance
         fields = ('Game','url')

class InvitationSerializer(serializers.ModelSerializer):
     class Meta:
          model = Invitation
          fields = "__all__"
     def create(self, request):
          i = Invitation.objects.create(GameInstance=request.get("GameInstance"),
                                        Target=request.get("Target"))
          i.save()
          return i
     
          
