from fastapi import FastAPI, APIRouter, HTTPException
import uvicorn
from pydantic import BaseModel, model_validator
   
app = FastAPI(title="Pydentic Validation!!")
routers = APIRouter(prefix="/validation", tags=["Validation"])

class ValidatePayload(BaseModel):
    email:str
    gender:str
    phone:str
    
    @model_validator(mode="after")
    def validate_demo(self) -> 'ValidatePayload':
        assert self.gender.lower() == "male", HTTPException(detail="Gender Must Be Male!!", status_code=422)
        return self
    
@routers.get("")
async def health_check():
    return "Good Health!!"

@routers.post("")
async def pydentic_validation(validate_payload: ValidatePayload):
    print(validate_payload)
    return "Validate Successfully!!"


app.include_router(routers)

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)