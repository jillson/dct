from django.conf.urls import include, url

from .views import GameListJSON, GameJSON

urlpatterns = [
    url(r'^game/$', GameListJSON.as_view(),name="gamelist"),
    url(r'^game/(?P<pk>\d+)$', GameJSON.as_view(),name="gamedetail"),
]
