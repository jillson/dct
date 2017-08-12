from django.test import TestCase,Client

from .models import Game, GameInstance, Row, Spot, Card, Deck

class testGameAPI(TestCase):
    def test_CreateInvalidGame(self):
        r = self.client.post("/api/gameInstances/",data={})
        self.assertEqual(r.status_code,400)
    def test_CreateInstance(self):
        g = Game.objects.create(Name="test")
        g.save()
        g2 = GameInstance.objects.create(Game=g)
        g2.save()
        r = self.client.post("/api/gameInstances/",data={"Game":g.id})
        #'http://testserver/api/games/{}/'.format(g.id)})
        self.assertEqual(r.status_code,201)
        r = self.client.get("/api/gameInstances/")
        self.assertContains(r,str(g.id))
    def test_BadGameDetails(self):
        r = self.client.get("/api/games/0/")
        self.assertEqual(r.status_code,404)
    def test_GameInfo(self):
        g = Game.objects.create(Name="test")
        g.save()
        r = self.client.get("/api/games/{}/".format(g.id))
        self.assertEqual(r.status_code,200)
    def test_GameDetails(self):
        g = Game.objects.create(Name="test")
        cards = [Card.objects.create(Name=chr(ord('a')+i)) for i in range(10)]
        deck = Deck.objects.create(Name="foo")
        deck.save()
        for c in cards:
            c.save()
            deck.Cards.add(c)
        deck.save()
        
        s = Spot.objects.create(Name="a",Deck=deck)
        s2 = Spot.objects.create()
        s.save()
        s2.save()
        aRow = Row.objects.create(Name="aRow",NewRow=True)
        bRow = Row.objects.create(Name="bRow")
        aRow.Spots.add(s)
        bRow.Spots.add(s2)
        aRow.save()
        bRow.save()
        g.Rows.add(aRow)
        g.Rows.add(bRow)
        g.save()
        r = self.client.get("/api/games/{}/".format(g.id))
        self.assertContains(r,"test")
        print (r.json())

class testGameInstanceAPI(TestCase):
    pass


class testInvites(TestCase):
    pass
