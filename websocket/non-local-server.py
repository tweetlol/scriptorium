import asyncio
import websockets

async def hello(websocket):
    incoming_payload = await websocket.recv()
    print(f">>> CLIENT: {incoming_payload}")

    response = f"GENERAL KENOBI, length of your message is {len(incoming_payload)}"

    await websocket.send(response)
    print(f"<<< SERVER: {response}")

async def main():
    local_ip = "10.0.0.14"
    port = 8765
    async with websockets.serve(hello, local_ip, port):
        await asyncio.Future()  #runs forever




if __name__ == "__main__":
    asyncio.run(main())