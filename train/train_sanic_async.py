# encoding: utf-8
"""
该文件主要测试sanic web框架 异步功能
1： 同时访问主页面 F12 查看主页面的响应时间
"""
import time
import asyncio
from sanic import Sanic
from sanic.response import json

app = Sanic(name="pytest")

@app.route("/index1")
async def test_async1(request):
    time.sleep(5)
    return json({"name": "hello world"})


async def task_sleep():
    print(f"sleep before {time.ctime()}")
    await asyncio.sleep(5)
    print(f"sleep after {time.ctime()}")
    pass


@app.route("/index2")
def test_async2(request):
    my_loop = request.app.loop
    my_loop.create_task(task_sleep())
    return json({"name": "hello world"})
    pass


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
    pass
