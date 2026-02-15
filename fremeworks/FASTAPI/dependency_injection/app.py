from fastapi import FastAPI, APIRouter, HTTPException, Depends, Header
from pydantic import BaseModel, EmailStr, Field, model_validator, field_validator
import datetime

app = FastAPI(title="Denpendency Injection!!")
routers = APIRouter(prefix="/with_denpendency", tags=["Dependency Injection"])

class PreCheckToDo(BaseModel):
    work: str
    duration: int
    start_time: datetime.datetime = Field(default_factory=datetime.datetime.now)

    @model_validator(mode="after")
    def validate_fields(self):
        if "ai" in self.work.lower():
            return self
        raise ValueError("AI task is acceptable only")

class PreCheckUsers(BaseModel):
    name: str
    email: EmailStr

    @field_validator("email", mode="after")
    @classmethod
    def drl_email_validator(cls, v):
        if v.endswith("@drreddys.com"):
            return v
        raise ValueError("Allow Drreddys Emails Only")

def dependency_system_users(todo: PreCheckToDo) -> int:
    return todo.duration

async def get_token(Authorization: str = Header(...)):
    if not Authorization.startswith("Bearer "):
        raise HTTPException(status_code=401)
    return Authorization

async def dependency_users(
    user: PreCheckUsers,
    token: str = Depends(get_token)
):
    return user

@routers.post("/todo")
async def my_todo(
    duration = Depends(dependency_system_users),
    user = Depends(dependency_users)
):
    return {"duration": duration, "user": user}

app.include_router(routers)

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)