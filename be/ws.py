import asyncio
import websockets
import logging

logging.basicConfig(level=logging.INFO)


async def handler(websocket):
    while True:
        try:
            message = await websocket.recv()
            print(message)

        except websockets.ConnectionClosedOK:
            break


async def main():
    async with websockets.serve(handler, "localhost", 8765):
        await asyncio.Future()  # run forever


asyncio.run(main())
