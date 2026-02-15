from fastapi import FastAPI, APIRouter, HTTPException, Depends
import uvicorn
from pydantic import BaseModel, model_validator 
import datetime

valid_user = ["ashu"] 

class PreCheckToDo(BaseModel):
    work: str
    duration: int
    start_time:datetime.datetime = datetime.datetime.now() 

    @model_validator(mode="after")
    def validate_fields(self) -> 'PreCheckToDo':
        if "ai" in self.work.lower(): return self
        raise HTTPException(detail="AI task is acceptable !!", status_code=422)
        
app = FastAPI(title="Denpendency Injection!!")
routers = APIRouter(prefix="/with_denpendency", tags=["Dependency Injection"])

@app.get("/health_check")
async def health_check():
    return "Good Heath!!"

async def dependenct_system_users():
    if "ashu" in valid_user:
        return valid_user
    raise HTTPException(detail="Not Valid User", status_code=401)

@routers.post("/todo")
async def my_todo(todo: PreCheckToDo, token:list = Depends(dependenct_system_users)):
    print(todo)
    print(token)
    return f"Added Todo {todo.work}"
    
app.include_router(routers)

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)