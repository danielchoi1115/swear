

from typing import List, Optional
import uvicorn
from fastapi import FastAPI, Response, WebSocket, WebSocketDisconnect, status, UploadFile, File, Request, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from datetime import datetime
import json
from pydantic import BaseModel
import router
import asyncio
from config import loop
from core.settings import Settings
from schema import Message
from app.connections import manager
settings = Settings(auth_key='aa', api_key='bb')
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    now = datetime.now()
    try:
        while True:
            data = await websocket.receive_text()
            message = Message(
                sendFrom=client_id,
                sendTo=111,
                time=now,
                message=str(data)
            )
            # print('data is',data)
            # await manager.broadcast(json.dumps(message))
            await router.produce(message)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        message = {
            "time": str(now),
            "client_id": client_id,
            "message": "offline"
        }
        await manager.broadcast(json.dumps(message))

    
    # await websocket.accept()
    # while True:
    #     data = await websocket.receive_text()
    #     print('data is',data)
    #     await websocket.send_text(f"Message text was: {data}")


app.include_router(router.route)
# def init():
#     uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)

# if __name__ in ("__main__"):
#     init()
