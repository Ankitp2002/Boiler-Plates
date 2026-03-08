from fastapi import FastAPI, WebSocket, WebSocketException
import uvicorn
from ml_routes import router as ml_router

app = FastAPI(title="ML Interface Orchestrator")

@app.get("/")
async def health_check():
    return "Good Health!!"

@app.websocket("/ws")
async def initiate_websocket(web_socket: WebSocket):
    try:
        await web_socket.accept()
        while True:
            user_data = await web_socket.receive()
            await web_socket.send_text("hello")

    except WebSocketException:
        await web_socket.close()

    except Exception as err:
        return str(err)


app.include_router(ml_router)


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)