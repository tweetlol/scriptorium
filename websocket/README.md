# WEBSOCKET

using py libraries:

- websockets
- asyncio

server.py opens a websocket at localhost on specified port

client.py can interact with the server via the websocket, allowing realtime updates

### ISSUES:

- server crashes if websocket is left open (no time specified)
