import fastapi

app = fastapi.FastAPI()

@app.get("/{name}")
async def get_name(name: str):
    return {"message":"Hello, {}".format(name)}