from django.test import TestCase,Client

from .models import Game, GameInstance, Row, Spot, Card

print ("We read tests.py")

class testGameAPI(TestCase):
    def test_CreateInvalidGame(self):
        r = self.client.post("/api/gameInstance/",id=0)
        self.assertEqual(r.status_code,404)
    def test_CreateInstance(self):
        g = Game.objects.create(Name="test")
        g.save()
        r = self.client.post("/api/gameInstance/",id=g.id)
        #self.assertEqual(r.status_code,301)
        import pdb
        pdb.set_trace()
    def test_BadGameDetails(self):
        r = self.client.get("/api/game/0")
        self.assertEqual(r.status_code,404)
    def test_GameInfo(self):
        g = Game.objects.create(Name="test")
        g.save()
        r = self.client.get("/api/game/0")
        self.assertEqual(r.status_code,200)
    def test_GameDetails(self):
        g = Game.objects.create(Name="test")
        s = Spot.objects.create(Name="a")
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
        r = self.client.get("/api/game/"+str(g.id))
        self.assertContains(r,"test")
        import pdb
        pdb.set_trace()

#class testGameInstanceAPI(TestCase):
#    pass
