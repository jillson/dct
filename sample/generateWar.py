import json

suits = ["Spades","Hearts","Clubs","Diamonds"]
values = ["Ace","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King"]
visibilities = ["all","flip","player1","player2","player3","player4"]

suittags = [{"model": "cards.tag", "fields": { "Name": suit}} for suit in suits]
valuetags = [{"model": "cards.tag", "fields": { "Name": value}} for value in values]

cards = [{"model": "cards.card", "fields": { "Name": "{} of {}".format(value,suit),"Tags": [[value],[suit]]}} for suit in suits for value in values]

deck = [{"model": "cards.deck","fields":{"Name":"Poker Deck","Cards": [[card["fields"]["Name"]] for card in cards]}}]

vs = [{"model": "cards.visibility", "fields":{"Name":v,"Description":""}} for v in visibilities]

pspots = [{"model":"cards.spot","fields": { "Name": "{} Draw".format(p.title()), "Drop": True}} for p in ["player1","player2"]]

espot = [{"model":"cards.spot","fields" :{ "Name": "Shared Draw", "Deck": ["Poker Deck"]}}]

spots = espot + pspots

prows = [{"model": "cards.row","fields": {
    "Name": "War {} Row".format(p.title()),
    "NewRow": False,
    "Visibility" : [p],
    "Spots": [["{} Draw".format(p.title())]]}} for p in ["player1","player2"]]

mrow = [{"model": "cards.row","fields": {
    "Name": "War Middle Row",
    "NewRow": False,
    "Visibility" : ["flip"],
    "Spots": [["Shared Draw"]]}}]

rows = prows + mrow

game = [{"model":"cards.game","fields":{"Name":"War","Rows":[["War Player1 Row"],["War Middle Row"],["War Player2 Row"]]}}]

toDump = suittags + valuetags + cards + deck + vs + spots + rows

print(json.dumps(toDump,indent=2))
