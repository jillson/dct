from channels import Channel,Group
from channels.sessions import channel_session
from .models import GameInstance, Game
import json

# Connected to chat-messages
def msg_consumer(message):
    Group("chat").send({
        "text": message.content['message'],
    })

def user_consumer(message):
    uid = message.channel_session.get('group')
    if uid:
        Group(uid).send({
            "text": message.content['message'],
        })
    else:
        print("Error, didn't find uid in ",message.channel_session)
        
# Connected to websocket.connect
@channel_session
def ws_connect(message):
    path = message.content['path'].strip("/")
    if path.find("chat") != -1:
        message.channel_session['group'] = "chat"
        Group("chat").add(message.reply_channel)
        message.reply_channel.send({"accept": True})
    elif path.find("user") != -1:
        gname = path.replace("/","")
        message.channel_session['group'] = gname
        try:
            uid = int(gname[4:])
        except ValueError:
            print("debug",gname)
            return
        #TODO:
        #get user object
        #get their invitations
        #get their active games
        #get list of games they can create
        games = {}
        games["invitations"] = []
        games["games"] = [g.id for g in Game.objects.all()]
        games["gis"] = []
        Group(gname).add(message.reply_channel)
        message.reply_channel.send({"text":json.dumps(games),"accept": True})
    else:
        print("Not sure what to do about path",path)

# Connected to websocket.receive
@channel_session
def ws_message(message):
    if message.channel_session['group'] == "chat":
        Channel("chat-messages").send({
            #"room": message.channel_session['room'],
            "message": message['text'],
        })
    else:
        print("Debug, we need to handle",message.channel_session,message.get("text"))
# Connected to websocket.disconnect
@channel_session
def ws_disconnect(message):
    Group(message.channel_session['group']).discard(message.reply_channel)
