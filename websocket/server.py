import asyncio
import websockets

async def hello(websocket):
    incoming_payload = await websocket.recv()
    print(f"Server received: {incoming_payload}")

    response = f"this is a response from the server to: \"{incoming_payload}\""

    await websocket.send(response)
    print(f"Server sent a response.")

async def main():
    port = 8765
    async with websockets.serve(hello, "localhost", port):
        await asyncio.Future()  #runs forever




if __name__ == "__main__":
    asyncio.run(main())