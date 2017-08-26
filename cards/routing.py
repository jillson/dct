from channels.routing import route
from .consumers import ws_connect, ws_message, ws_disconnect, msg_consumer, user_consumer

channel_routing = [
    route("websocket.connect", ws_connect),
    route("websocket.receive", ws_message),
    route("websocket.disconnect", ws_disconnect),
    route("chat-messages", msg_consumer),
    route("user-messages", user_consumer),
]
