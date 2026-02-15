from fastapi import FastAPI
import uvicorn 
from utils import LRUCache, _Node
from pydantic import BaseModel

app = FastAPI(title="Manual Cache APP!!")
_cache = LRUCache(10)

class CacheScema(BaseModel):
    _cache_key: str
    _cache_value: str
    
@app.get("/health_check")
async def health_check():
    return "Good Health..."

@app.get("/value")
async def get_value():
    return "Valus"

@app.post("/value")
async def set_value(cachescema: CacheScema):
    _value_node = _Node(cachescema._cache_key, cachescema._cache_value)

    _cache._add_to_front(_value_node)
    _cache._move_to_front(_value_node)
    
    return "Successfully Added..."

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
    