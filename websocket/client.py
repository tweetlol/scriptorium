import asyncio
import websockets
import time

async def send_data():
    uri = "ws://localhost:8765" # where to send
    async with websockets.connect(uri) as websocket:
        payload = input(50*"#" + f"\nEnter message to be sent via {websocket}:\n")

        await websocket.send(payload)

        response = await websocket.recv()
        print(f"Client received: {response}")




if __name__ == "__main__":
        asyncio.run(send_data())