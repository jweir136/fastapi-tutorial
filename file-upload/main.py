import fastapi

app = fastapi.FastAPI()

@app.post("/file/upload")
async def upload_file(fileb: fastapi.UploadFile = fastapi.File()):
    return {"message":"{}".format(fileb)}