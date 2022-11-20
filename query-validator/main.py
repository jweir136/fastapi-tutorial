import fastapi

app = fastapi.FastAPI()

"""
validator makes sure that query strings have at least 1 character and no
more than 100 characters.
"""
@app.get("/user")
async def user(name: str = fastapi.Query(min_length=1, max_length=100)):
    return {"message":"Hello, {}".format(name)}