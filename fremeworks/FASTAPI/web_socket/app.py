from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import uvicorn

app = FastAPI(title="Web Socket APP !!") 

@app.get("/health_check")
async def health_check():
    return "Good Health!!"

@app.websocket("/ws")
async def initiate_websocket(websocket: WebSocket):
    try:
        await websocket.accept()
        while True:
            tunnal_message = await websocket.receive()
            await websocket.send_text(f"Recived Message was: {tunnal_message}")
    except WebSocketDisconnect:
        pass
    except Exception as err:
        pass
    
if __name__ == "__main__":
    uvicorn.run("app:app", host = "127.0.0.1", port = 8000, reload = True)


