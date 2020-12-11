from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def poetry():
    return {"message": "Hello world"}



