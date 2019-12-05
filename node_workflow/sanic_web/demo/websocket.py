import asyncio
import datetime
import random
import websockets

async def time(websocket, path):
    while True:
        color_list = ['#c23531', '#2f4554', '#61a0a8', '#d48265', '#91c7ae', '#749f83', '#ca8622', '#bda29a', '#6e7074',
                '#546570', '#c4ccd3']
        for cl in color_list:

            await websocket.send(cl)
            await asyncio.sleep(random.random() * 1)

start_server = websockets.serve(time, "127.0.0.1", 9010)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()