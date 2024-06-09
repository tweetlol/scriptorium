import asyncio
import websockets
import time

async def send_data():
    uri = "ws://10.0.0.14:8765" # where to send
    async with websockets.connect(uri) as websocket:
        print(100*"#" + f"\nEnter message to be sent via {websocket}:\n")
        payload = input(">>> CLIENT: ")

        await websocket.send(payload)

        response = await websocket.recv()
        print(f"<<< SERVER: {response}")




if __name__ == "__main__":
        asyncio.run(send_data())