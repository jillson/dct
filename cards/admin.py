from django.contrib import admin

from .models import *


admin.site.register(Tag)
admin.site.register(Card)
admin.site.register(Deck)
admin.site.register(Spot)
admin.site.register(Visibility)
admin.site.register(Row)
admin.site.register(Game)
admin.site.register(GameInstance)
admin.site.register(Invitation)
