# encoding:utf-8
"""sanic web框架测试"""

from sanic import Sanic
from sanic.response import text, json
app = Sanic()

@app.route("/")
async def test(request):
    return json({ "hello": " world "})

@app.websocket('/feed')
async def feed(request, ws):
    while True:
        data = 'hello!'
        print('Sending: ' + data)
        await ws.send(data)
        data = await ws.recv()
        print('Received: ' + data)

app.run(host="0.0.0.0", port=8000, debug=True)
