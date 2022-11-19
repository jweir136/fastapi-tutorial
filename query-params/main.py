import fastapi

app = fastapi.FastAPI()

@app.get("/user/greet")
async def greet_user(name: str):
    return {
        "message":"Hello, {}".format(name)
    }