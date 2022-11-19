import fastapi
from pydantic import BaseModel

# use objects to represent request bodies passed using POST requests.
class User(BaseModel):
    name: str
    age: int

app = fastapi.FastAPI()

@app.post("/user")
async def user(user: User):
    return {"message":user}