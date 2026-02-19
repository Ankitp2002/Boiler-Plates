from fastapi import FastAPI, APIRouter, WebSocket, WebSocketException
import uvicorn

app = FastAPI(title="ML Interface Orchestrator")
@app.get("/")
def health_check():
    return "Good Health!!"

routers = APIRouter(prefix="/ml", tags=["ML API"])

@routers.get("")
async def initiate_model():
    return "Initiate Successfully!!"

@app.websocket("/ws")
async def initiate_socket(web_socket:WebSocket):
    try:
        await web_socket.accept()
        while True:
            user_data = await web_socket.receive()
            await web_socket.send_text("hello")
            
    except WebSocketException:
        await web_socket.close()
    
    except Exception as err:
        return str(err)    
        
app.include_router(routers)

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)