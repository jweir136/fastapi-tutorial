import fastapi

app = fastapi.FastAPI()

@app.get("/")
async def root():
    return {"message":"hello, world!"}

@app.post("/form")
async def send_form(name: str = fastapi.Form()):
    return {"message":"Hello, {}".format(name)}