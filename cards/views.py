

from rest_framework import viewsets
from .serializers import GameSerializer, GameInstanceSerializer
from .models import Game, GameInstance

class GameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows games to be viewed or edited.
    """
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GameInstanceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows games to be viewed or edited.
    """
    queryset = GameInstance.objects.all()
    serializer_class = GameInstanceSerializer
