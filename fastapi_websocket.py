# -*-coding:utf-8-*-
from typing import Optional

from fastapi import FastAPI, WebSocket, Query, Cookie, Depends
from fastapi.responses import HTMLResponse
import uvicorn
app = FastAPI()
html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""
# @app.get("/")
# async def get():
#     return HTMLResponse(html)
#
# @app.websocket("/ws")
# async def websocket_endpoint(websocket:WebSocket):
#     await websocket.accept()
#     while True:
#         data = await websocket.receive_text()
#         await websocket.send_text(f"消息是:{data}")

"""
使用Depends及其他¶
在 WebSocket 端点中，您可以导入fastapi并使用：
Depends
Security
Cookie
Header
Path
Query
"""

index = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <label>Item ID: <input type="text" id="itemId" autocomplete="off" value="foo"/></label>
            <label>Token: <input type="text" id="token" autocomplete="off" value="some-key-token"/></label>
            <button onclick="connect(event)">Connect</button>
            <hr>
            <label>Message: <input type="text" id="messageText" autocomplete="off"/></label>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
        var ws = null;
            function connect(event) {
                var itemId = document.getElementById("itemId")
                var token = document.getElementById("token")
                ws = new WebSocket("ws://localhost:8000/items/" + itemId.value + "/ws?token=" + token.value);
                ws.onmessage = function(event) {
                    var messages = document.getElementById('messages')
                    var message = document.createElement('li')
                    var content = document.createTextNode(event.data)
                    message.appendChild(content)
                    messages.appendChild(message)
                };
                event.preventDefault()
            }
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""
# from fastapi import status
# @app.get("/")
# async def get():
#     return HTMLResponse(index)
# async def get_cookie_or_token(
#         websocket:WebSocket,
#         session:Optional[str] = Cookie(None),
#         token:Optional[str] =Query(None)
# ):
#     if session is None and token is None:
#         await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
#         return session or token
# @app.websocket("/items/{item_id}/ws")
# async def websocket_endpoint(
#         websocket:WebSocket,
#         item_id:str,
#         q:Optional[str] = None,
#         cookie_or_token:str=Depends(get_cookie_or_token),
#                              ):
#     await websocket.accept()
#     while True:
#         data = await websocket.receive_text()
#         await websocket.send_text(
#             f"Session cookie or query token value is: {cookie_or_token}"
#         )
#         if q is not None:
#             await websocket.send_text(f"Query parameter q is: {q}")
#         await websocket.send_text(f"Message text was: {data}, for item ID: {item_id}")
"""
处理断开连接和多个客户端
"""

from typing import List
from fastapi import WebSocketDisconnect
home = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <h2>Your ID: <span id="ws-id"></span></h2>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var client_id = Date.now()
            document.querySelector("#ws-id").textContent = client_id;
            var ws = new WebSocket(`ws://localhost:8000/ws/${client_id}`);
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""

#创建连接管理类
class ConnectionManager:
    def __init__(self):
        self.active_connections:List[WebSocket] = []
    async def connect(self,websocket:WebSocket):
        await websocket.accept()
        #添加websocket对象
        self.active_connections.append(websocket)
    def disconnect(self,websocket:WebSocket):
        self.active_connections.remove(websocket)
    async def send_persional_message(self,message:str,websocket:WebSocket):
        await websocket.send_text(message)
    async def broadcast(self,message:str):
        for connection in self.active_connections:
            await connection.send_text(message)
manager = ConnectionManager()

@app.get("/")
async def get():
    return HTMLResponse(home)
@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket:WebSocket,client_id:int):
    print(client_id)
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_persional_message(f"You wrote: {data}", websocket)
            await manager.broadcast(f"Client #{client_id} says: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} left the chat")


if __name__ == '__main__':
    uvicorn.run("fastapi_websocket:app")

